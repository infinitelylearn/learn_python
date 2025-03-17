# Financial Domain Integration

Always connect Python concepts to financial markets and algorithmic trading. This makes learning more relevant to the user's goals and creates practical mental frameworks.

## Domain Connection Guidelines

1. **Basic Python**: Use market data examples (e.g., lists of prices, dictionaries of assets)
2. **Data Structures**: Frame in terms of order books, price series, trading signals
3. **Functions/OOP**: Design trading strategies, risk management components
4. **Performance**: Optimize for real-time market data processing
5. **API/Integration**: Connect to market data sources, broker interfaces

## Example Application Table

| Python Concept      | Trading Application                                   |
|---------------------|------------------------------------------------------|
| Lists               | Time series of closing prices                        |
| Dictionaries        | Asset attributes (symbol, price, volume)             |
| Functions           | Signal generation, risk calculation                  |
| Classes             | Strategy objects, instrument definitions             |
| NumPy arrays        | Fast calculation of technical indicators             |
| Pandas DataFrames   | OHLCV data manipulation and analysis                 |
| List comprehensions | Filtering trade signals                              |
| Error handling      | Robustness against API failures                      |

## Domain-Specific Examples

### Basic Data Types
```python
# Use financial examples for data types
prices = [1.2345, 1.2350, 1.2360, 1.2355]  # List of price points
symbols = ["EURUSD", "GBPUSD", "USDJPY"]   # Currency pairs
is_market_open = True                      # Boolean for market status
```

### Dictionaries
```python
# Asset information with dictionaries
forex_pairs = {
    "EURUSD": {"bid": 1.0823, "ask": 1.0825, "spread": 0.0002},
    "GBPUSD": {"bid": 1.2650, "ask": 1.2654, "spread": 0.0004},
    "USDJPY": {"bid": 107.50, "ask": 107.53, "spread": 0.03}
}
```

### Functions
```python
def calculate_rsi(prices, period=14):
    """Calculate the Relative Strength Index."""
    # Implementation
    return rsi_values

def compute_position_size(account_balance, risk_percent, stop_loss_pips):
    """Calculate position size based on risk management rules."""
    # Implementation
    return position_size
```

### Control Flow
```python
# Trading decision based on conditional logic
if current_price > moving_average and rsi < 30:
    # Potential buy signal
    if volume > average_volume * 1.5:
        execute_buy_order()
    else:
        add_to_watchlist()
else:
    # No trading opportunity
    monitor_market()
```

### Classes
```python
class TradingStrategy:
    def __init__(self, symbol, timeframe):
        self.symbol = symbol
        self.timeframe = timeframe
        self.indicators = {}
    
    def add_indicator(self, name, params):
        # Add indicator to strategy
        pass
    
    def generate_signals(self, data):
        # Analyze data and generate trading signals
        pass
```

### Exception Handling
```python
try:
    price_data = api.get_historical_data(symbol, start_date, end_date)
    # Process data
except ConnectionError:
    # Handle API connection issues
    log_error("Connection to data provider failed")
    use_cached_data()
except RateLimitError:
    # Handle API rate limiting
    wait_and_retry(60)  # Wait 60 seconds before retry
```

## Domain Adaptation by Topic

When teaching specific topics, frame them within the user's preferred financial domain:

### For Forex Examples
- Focus on currency pairs (EURUSD, GBPUSD)
- Use pip values and spread concepts
- Highlight rollover and swap rates
- Emphasize time zone considerations for market hours

### For Stock Market Examples
- Use company tickers and sectors
- Incorporate dividend adjustments
- Show market cap and P/E ratio calculations
- Discuss market hours and pre/post market

### For Cryptocurrency Examples
- Use major coins and trading pairs (BTC/USD, ETH/BTC)
- Incorporate blockchain concepts when relevant
- Highlight 24/7 market characteristics
- Discuss volatility and liquidity differences

## Cross-Topic Integration with Financial Examples

When integrating review topics with new material, use financial examples that combine both:

### Example: Reviewing Lists while Teaching Functions
```python
def calculate_drawdown(price_list):  # New topic: functions
    """Calculate maximum drawdown from a list of prices."""
    peak = price_list[0]  # Review topic: list indexing
    max_drawdown = 0
    
    for price in price_list:  # Review topic: list iteration
        if price > peak:
            peak = price
        drawdown = (peak - price) / peak * 100
        if drawdown > max_drawdown:
            max_drawdown = drawdown
            
    return max_drawdown

# Using the function with a price list
btc_prices = [42300, 43100, 41500, 40200, 41800]  # Review topic: list creation
max_dd = calculate_drawdown(btc_prices)  # New topic: function calls
print(f"Maximum drawdown: {max_dd:.2f}%")
```

This example simultaneously teaches function definition and calls while reinforcing list concepts, all within a relevant financial context.