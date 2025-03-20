# bollinger_cython.pyx
# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True, nonecheck=False

import numpy as np
cimport numpy as np
from libc.math cimport sqrt

# Define C functions for speed
cdef double calc_mean(double[:] data, int window) nogil:
    """Calculate mean of array"""
    cdef double total = 0.0
    cdef int i
    
    for i in range(window):
        total += data[i]
    
    return total / window

cdef double calc_std(double[:] data, int window, double mean) nogil:
    """Calculate standard deviation"""
    cdef double total = 0.0
    cdef int i
    
    for i in range(window):
        total += (data[i] - mean) * (data[i] - mean)
    
    return sqrt(total / (window - 1))  # Sample standard deviation

def bollinger_bands_cython(np.ndarray[double, ndim=1] prices, int window=20, double num_std=2.0):
    """Calculate Bollinger Bands using optimized Cython code"""
    cdef int n = len(prices)
    cdef int num_bands = n - window + 1
    
    # Pre-allocate arrays for results
    cdef np.ndarray[double, ndim=1] sma = np.zeros(num_bands, dtype=np.float64)
    cdef np.ndarray[double, ndim=1] upper = np.zeros(num_bands, dtype=np.float64)
    cdef np.ndarray[double, ndim=1] lower = np.zeros(num_bands, dtype=np.float64)
    
    # Create a memory view for faster access
    cdef double[:] prices_view = prices
    cdef double[:] sma_view = sma
    cdef double[:] upper_view = upper
    cdef double[:] lower_view = lower
    
    cdef int i
    cdef double mean, std
    
    # Calculate bands using optimized C code
    for i in range(num_bands):
        # Calculate mean for this window
        mean = calc_mean(prices_view[i:i+window], window)
        sma_view[i] = mean
        
        # Calculate standard deviation
        std = calc_std(prices_view[i:i+window], window, mean)
        
        # Calculate bands
        upper_view[i] = mean + (std * num_std)
        lower_view[i] = mean - (std * num_std)
    
    # Package results in same format as other implementations
    results = []
    for i in range(num_bands):
        idx = i + window - 1
        results.append((idx, prices[idx], sma[i], upper[i], lower[i]))
    
    return results
