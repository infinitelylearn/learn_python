import random
import time
import gc
import tracemalloc
from collections import deque
from statistics import mean, stdev
import numpy as np

# Try to import optional libraries
try:
    import numba
    HAVE_NUMBA = True
except ImportError:
    HAVE_NUMBA = False
    print("Numba not available. Install with: conda install numba")

try:
    import talib
    HAVE_TALIB = True
except ImportError:
    HAVE_TALIB = False
    print("TA-Lib not available.")

# Try to import the cython module
try:
    import bollinger_cython
    HAVE_CYTHON = True
    print("✅ Cython implementation loaded successfully!")
except ImportError:
    HAVE_CYTHON = False
    print("❌ Cython module not found. Make sure you've compiled it with 'python setup.py build_ext --inplace'")

# Memory tracking function
def track_memory_usage(func, *args, **kwargs):
    """Track peak memory usage of a function using tracemalloc"""
    # Force garbage collection before measurement
    gc.collect()
    
    # Start tracking memory allocations
    tracemalloc.start()
    
    # Get current memory usage
    start_mem = tracemalloc.get_traced_memory()[0] / (1024 * 1024)  # Convert to MB
    
    # Run the function
    start_time = time.time()
    result = func(*args, **kwargs)
    execution_time = time.time() - start_time
    
    # Get peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    current_mb = current / (1024 * 1024)  # Convert to MB
    peak_mb = peak / (1024 * 1024)        # Convert to MB
    
    # Memory used during function execution
    mem_used = current_mb - start_mem
    
    # Stop tracking memory allocations
    tracemalloc.stop()
    
    return result, execution_time, mem_used, peak_mb

# Generate price data
def generate_price_data(size=10000, start_price=100.0, volatility=0.02):
    """Generate random price data with a random walk pattern"""
    prices = [start_price]
    for _ in range(size - 1):
        # Random price movement with some momentum
        change_pct = random.normalvariate(0, volatility)
        new_price = prices[-1] * (1 + change_pct)
        # Ensure price doesn't go below 1
        prices.append(max(new_price, 1.0))
    return prices

# Original implementation using list slicing
def bollinger_bands_list(prices, window=20, num_std=2):
    """Generate Bollinger Bands from price data using list slicing"""
    results = []
    if len(prices) < window:
        return results
    
    for i in range(window, len(prices) + 1):
        # Get the current window of prices
        current_window = prices[i-window:i]
        
        # Calculate SMA (Simple Moving Average)
        sma = mean(current_window)
        
        # Calculate standard deviation
        std = stdev(current_window)
        
        # Calculate upper and lower bands
        upper_band = sma + (std * num_std)
        lower_band = sma - (std * num_std)
        
        # Current price
        current_price = prices[i-1]
        
        # Store the results
        results.append((i-1, current_price, sma, upper_band, lower_band))
    
    return results

# Deque implementation
def bollinger_bands_deque(prices, window=20, num_std=2):
    """Generate Bollinger Bands from price data using a deque sliding window"""
    results = []
    if len(prices) < window:
        return results
    
    # Create a deque for our sliding window
    price_window = deque(maxlen=window)
    
    # Fill window with initial prices
    for i in range(window-1):
        price_window.append(prices[i])
    
    # Process remaining prices
    for i in range(window-1, len(prices)):
        # Add current price to the window
        price_window.append(prices[i])
        
        # Calculate SMA
        sma = mean(price_window)
        
        # Calculate standard deviation
        std = stdev(price_window)
        
        # Calculate bands
        upper_band = sma + (std * num_std)
        lower_band = sma - (std * num_std)
        
        # Store results
        results.append((i, prices[i], sma, upper_band, lower_band))
    
    return results

# NumPy implementation
def bollinger_bands_numpy(prices, window=20, num_std=2):
    """Generate Bollinger Bands using NumPy vectorized operations"""
    results = []
    if len(prices) < window:
        return results
    
    # Convert to numpy array
    prices_array = np.array(prices)
    
    # Preallocate arrays
    sma_values = np.zeros(len(prices) - window + 1)
    std_values = np.zeros(len(prices) - window + 1)
    
    # Calculate SMA and STD for each window
    for i in range(len(prices) - window + 1):
        window_slice = prices_array[i:i+window]
        sma_values[i] = np.mean(window_slice)
        std_values[i] = np.std(window_slice, ddof=1)  # ddof=1 for sample standard deviation
    
    # Calculate bands
    upper_bands = sma_values + (std_values * num_std)
    lower_bands = sma_values - (std_values * num_std)
    
    # Package results
    for i in range(len(sma_values)):
        idx = i + window - 1
        results.append((idx, prices[idx], sma_values[i], upper_bands[i], lower_bands[i]))
    
    return results

# More efficient NumPy implementation using rolling window
def bollinger_bands_numpy_rolling(prices, window=20, num_std=2):
    """Generate Bollinger Bands using NumPy with a rolling window approach"""
    if len(prices) < window:
        return []
    
    # Convert to numpy array
    prices_array = np.array(prices)
    
    # Use numpy's rolling window functions
    # To get rolling mean, we need to calculate cumulative sum and divide
    cs = np.cumsum(np.insert(prices_array, 0, 0))
    sma_values = (cs[window:] - cs[:-window]) / window
    
    # For standard deviation, we need to use a sliding window
    std_values = np.array([np.std(prices_array[i:i+window], ddof=1) for i in range(len(prices) - window + 1)])
    
    # Calculate bands
    upper_bands = sma_values + (std_values * num_std)
    lower_bands = sma_values - (std_values * num_std)
    
    # Package results
    results = []
    for i in range(len(sma_values)):
        idx = i + window - 1
        results.append((idx, prices[idx], sma_values[i], upper_bands[i], lower_bands[i]))
    
    return results

# Highly optimized NumPy implementation
def bollinger_bands_numpy_ultra(prices, window=20, num_std=2):
    """Ultra-optimized Bollinger Bands using NumPy stride tricks"""
    if len(prices) < window:
        return []
    
    # Convert to numpy array
    prices_array = np.array(prices, dtype=np.float64)
    n = len(prices_array)
    
    # Use stride tricks for efficient rolling window
    try:
        from numpy.lib.stride_tricks import sliding_window_view
        windows = sliding_window_view(prices_array, window)
        
        # Calculate SMA and STD using vectorized operations
        sma_values = np.mean(windows, axis=1)
        std_values = np.std(windows, axis=1, ddof=1)
    except (ImportError, AttributeError):
        # Fallback for older NumPy versions
        sma_values = np.zeros(n - window + 1)
        std_values = np.zeros(n - window + 1)
        
        for i in range(n - window + 1):
            window_slice = prices_array[i:i+window]
            sma_values[i] = np.mean(window_slice)
            std_values[i] = np.std(window_slice, ddof=1)
    
    # Calculate bands
    upper_bands = sma_values + (std_values * num_std)
    lower_bands = sma_values - (std_values * num_std)
    
    # Package results
    results = []
    for i in range(len(sma_values)):
        idx = i + window - 1
        results.append((idx, prices[idx], float(sma_values[i]), float(upper_bands[i]), float(lower_bands[i])))
    
    return results

# If Numba is available, define a Numba-accelerated version
if HAVE_NUMBA:
    @numba.jit(nopython=True)
    def _calculate_bollinger_numba(prices, window, num_std):
        """Numba-optimized Bollinger Bands calculation"""
        n = len(prices)
        result_indices = np.zeros(n - window + 1, dtype=np.int64)
        result_prices = np.zeros(n - window + 1)
        result_sma = np.zeros(n - window + 1)
        result_upper = np.zeros(n - window + 1)
        result_lower = np.zeros(n - window + 1)
        
        for i in range(n - window + 1):
            # Get window slice
            window_sum = 0.0
            for j in range(window):
                window_sum += prices[i+j]
            
            # Calculate mean
            window_mean = window_sum / window
            
            # Calculate standard deviation
            window_var = 0.0
            for j in range(window):
                window_var += (prices[i+j] - window_mean) ** 2
            window_var /= (window - 1)  # Sample variance
            window_std = window_var ** 0.5  # Sample standard deviation
            
            # Store results
            idx = i + window - 1
            result_indices[i] = idx
            result_prices[i] = prices[idx]
            result_sma[i] = window_mean
            result_upper[i] = window_mean + (window_std * num_std)
            result_lower[i] = window_mean - (window_std * num_std)
        
        return result_indices, result_prices, result_sma, result_upper, result_lower
    
    def bollinger_bands_numba(prices, window=20, num_std=2):
        """Generate Bollinger Bands using Numba-accelerated functions"""
        if len(prices) < window:
            return []
        
        # Convert to numpy array
        prices_array = np.array(prices, dtype=np.float64)
        
        # Use Numba-optimized function
        indices, prices_result, sma, upper, lower = _calculate_bollinger_numba(prices_array, window, num_std)
        
        # Package results
        results = []
        for i in range(len(indices)):
            results.append((int(indices[i]), float(prices_result[i]), float(sma[i]), float(upper[i]), float(lower[i])))
        
        return results

# If TA-Lib is available, define a TA-Lib version
if HAVE_TALIB:
    def bollinger_bands_talib(prices, window=20, num_std=2):
        """Generate Bollinger Bands using TA-Lib"""
        if len(prices) < window:
            return []
        
        # Convert to numpy array
        prices_array = np.array(prices)
        
        # Calculate Bollinger Bands using TA-Lib
        upper, middle, lower = talib.BBANDS(prices_array, 
                                           timeperiod=window, 
                                           nbdevup=num_std, 
                                           nbdevdn=num_std, 
                                           matype=0)  # 0 for simple moving average
        
        # Package results (TA-Lib returns full arrays with NaN for undefined values)
        results = []
        for i in range(window-1, len(prices)):
            if not np.isnan(middle[i]):
                results.append((i, prices[i], middle[i], upper[i], lower[i]))
        
        return results

# Wrapper for Cython function to handle input type conversion
def bollinger_bands_cython_wrapper(prices, window=20, num_std=2):
    """Wrapper for Cython function to handle input type conversion"""
    if len(prices) < window:
        return []
    
    # Convert to numpy array if it's not already one
    if not isinstance(prices, np.ndarray):
        prices = np.array(prices, dtype=np.float64)
    
    # Call the actual Cython function
    return bollinger_cython.bollinger_bands_cython(prices, window, num_std)

def run_benchmark(sizes=[10000], window_sizes=[20, 50, 100, 200]):
    """Run benchmark of all available Bollinger Bands implementations"""
    # Define all implementations
    implementations = [
        ("List", bollinger_bands_list),
        ("Deque", bollinger_bands_deque),
        ("NumPy Basic", bollinger_bands_numpy),
        ("NumPy Rolling", bollinger_bands_numpy_rolling),
        ("NumPy Ultra", bollinger_bands_numpy_ultra),
    ]
    
    if HAVE_NUMBA:
        implementations.append(("Numba", bollinger_bands_numba))
    
    if HAVE_CYTHON:
        implementations.append(("Cython", bollinger_bands_cython_wrapper))
    
    if HAVE_TALIB:
        implementations.append(("TA-Lib", bollinger_bands_talib))
    
    for size in sizes:
        print(f"\nBenchmarking with {size} prices")
        print("=" * 90)
        prices = generate_price_data(size)
        
        for window in window_sizes:
            print(f"\nWindow Size: {window}")
            print("-" * 90)
            print(f"{'Implementation':<15}{'Time (s)':<12}{'Mem Used (MB)':<15}{'Peak Mem (MB)':<15}{'Speedup':<12}{'Mem Ratio':<12}")
            print("-" * 90)
            
            list_time = None
            list_mem_used = None
            reference_results = None
            
            # For each implementation, run a fresh memory test
            for name, func in implementations:
                # For JIT compilers, do a warm-up run to compile
                if name in ["Numba", "Cython"]:
                    if name == "Cython":
                        # For Cython, we need to convert to numpy array
                        warm_up_prices = np.array(prices[:1000], dtype=np.float64)
                    else:
                        warm_up_prices = prices[:1000]
                    _ = func(warm_up_prices, window=min(window, 20))
                
                try:
                    # Run with memory tracking
                    results, exec_time, mem_used, peak_mem = track_memory_usage(func, prices, window, num_std=2)
                    
                    # Store list implementation results as reference
                    if name == "List":
                        list_time = exec_time
                        list_mem_used = max(0.001, mem_used)  # Avoid division by zero
                        reference_results = results
                    
                    # Calculate relative performance
                    if list_time is not None and list_time > 0:
                        speedup = list_time / exec_time
                    else:
                        speedup = float('nan')
                        
                    if list_mem_used is not None and list_mem_used > 0:
                        mem_ratio = mem_used / list_mem_used
                    else:
                        mem_ratio = float('nan')
                    
                    # Verify results match reference (just check a few values)
                    if reference_results and len(results) > 0:
                        if len(reference_results) != len(results):
                            print(f"WARNING: {name} result length ({len(results)}) doesn't match reference ({len(reference_results)})")
                        elif abs(reference_results[0][2] - results[0][2]) > 0.01:
                            print(f"WARNING: {name} SMA values may not match reference implementation!")
                    
                    print(f"{name:<15}{exec_time:<12.6f}{mem_used:<15.2f}{peak_mem:<15.2f}{speedup:<12.2f}x{mem_ratio:<12.4f}x")
                    
                except Exception as e:
                    print(f"{name:<15}{'Failed':<12}{str(e)}")

if __name__ == "__main__":
    print("Bollinger Bands Performance Benchmark")
    print("=====================================")
    print("\nChecking available implementations:")
    
    # Run the benchmark
    print("\nRunning benchmark...")
    run_benchmark(sizes=[10000], window_sizes=[20, 50, 100, 200])
    
    # Optional larger test
    larger_test = input("\nDo you want to run with a larger dataset (50,000 prices)? (y/n): ")
    if larger_test.lower() in ['y', 'yes']:
        run_benchmark(sizes=[50000], window_sizes=[20, 100, 200])