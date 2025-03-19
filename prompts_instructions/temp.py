stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
prices = [184.92, 417.88, 174.13, 178.15, 474.88]
prices2 = [184.92, 417.88, 174.13, 178.15, 474.88, 123.2, 345.3, 123.3, 413.7, 754.3, 184.92, 417.88, 174.13, 178.15, 474.88, 123.2, 345.3, 123.3, 413.7, 754.3, 184.92, 417.88, 174.13, 178.15, 474.88, 123.2, 345.3, 123.3, 413.7, 754.3]
pe_ratios = [32.6, 38.2, 26.4, 59.8, 25.1]
sectors = ['Tech', 'Tech', 'Tech', 'Consumer', 'Tech']


# 1. 
# a) 
stock_price = [(stock, price) for stock, price in zip(stocks, prices) if price > 200]

# b) 
stock_value_category = {stock: "high_value" if price > 300 else "standard" for stock, price in zip(stocks, prices)}

# c) 
stock_pe_sector = {stock: {"price: ": price, "pe_ratio": pe_ratio, "sector": sector} for stock, price, pe_ratio, sector in zip(stocks, prices, pe_ratios, sectors)}

# 2.
# a) Write a generator function called moving_average that takes a list of prices and a window size, and yields the moving average for each window of prices.
def moving_average(prices, window_size=3):

    if window_size < 1:
        print("Window size needs to be more than 0")
        return None

    for i in range(window_size, len(prices)):

        avg = sum(prices[i - window_size:i])/window_size
        yield avg

# sma3 = moving_average(prices2)
# for sma in sma3:
#     print(sma)

# b) Write a generator function called price_momentum that:
# Takes a list of daily prices
# Calculates the 5-day and 20-day moving averages (using your function from part a)
# Yields 'bullish', 'bearish', or 'neutral' signals based on the relationship between the short and long moving averages

def price_momentum(prices, ma1=5, ma2=20):
    window_difference = ma2 - ma1
    prices_short = prices[window_difference:]
    sma5 = moving_average(prices_short, window_size=ma1)
    sma20 = moving_average(prices, window_size=ma2)

    for ma5, ma20 in zip(sma5, sma20):
        if ma5 > ma20:
            signal = 'bullish'
        elif ma5 < ma20:
            signal = 'bearish'
        else:
            signal = 'neutral'

        yield signal

pm = price_momentum(prices2)

# for signal in pm:
#     print(signal)

# Exercise 3: Generator Pipeline
# Create a series of generator functions that form a data processing pipeline:

# a) First function parse_trade_data receives a list of strings in the format "SYMBOL,PRICE,VOLUME" and yields tuples of (symbol, float(price), int(volume))
def parse_trade_data(trades):
    for trade in trades:
        symbol, price, volume = trade.strip().split(',')
        yield (symbol, float(price), int(volume))

# b) Second function filter_trades takes the output of the first function and yields only trades with volume > 10000
def filter_trades(trade_data, volume_filter=10000):
    for symbol, price, volume in trade_data:
        if volume > volume_filter:
            yield (symbol, price, volume)
    

# c) Third function calculate_value takes the output of the second function and yields tuples of (symbol, price*volume) representing the total trade value

def calculate_value(filtered_trades):
    for symbol, price, volume in filtered_trades:
        yield symbol, price*volume

# d) Show how you would connect these functions in a pipeline and process this data:
trades = [
    "AAPL,186.25,12500",
    "MSFT,415.50,8200",
    "GOOGL,175.30,15000",
    "AMZN,178.90,5000",
    "META,475.20,11000"
]
parse = parse_trade_data(trades)

filtered = filter_trades(parse)    

calculate = calculate_value(filtered)

print("High volume trades:")
for symbol, total_value in calculate:
    print(f"{symbol}: ${total_value:,.2f}")


# Exercise 4: Comprehension with Conditionals
# Given the following stock performance data:
performance = [
    {'symbol': 'AAPL', 'return': 12.3, 'volatility': 15.2, 'beta': 1.2},
    {'symbol': 'MSFT', 'return': 8.7, 'volatility': 12.8, 'beta': 1.1},
    {'symbol': 'GOOGL', 'return': 15.6, 'volatility': 18.5, 'beta': 1.3},
    {'symbol': 'AMZN', 'return': 5.2, 'volatility': 22.3, 'beta': 1.5},
    {'symbol': 'META', 'return': 19.8, 'volatility': 25.1, 'beta': 1.7},
]

# a) Create a list comprehension that selects stocks with return/volatility ratio > 0.7 (a simple Sharpe-like measure)
high_rvr = [perf['symbol'] for perf in performance if perf['return'] / perf['volatility'] > 0.7]

# b) Create a dictionary comprehension that categorizes stocks as 'aggressive' (beta > 1.3),
# 'moderate' (beta between 1.1 and 1.3), or 'defensive' (beta < 1.1)
stock_vola = {
    perf['symbol']: ("aggressive" if perf['beta'] > 1.3 else 
                   "moderate" if 1.1 <= perf['beta'] <= 1.3 else 
                   "defensive")
    for perf in performance
}

print(stock_vola)