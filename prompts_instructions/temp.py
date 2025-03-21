class StockAnalyzer:
    '''
    Stores historical price data for a stock.
    Calculates basic statistics like mean, median, and standard deviation.
    Includes a method to calculate daily returns.
    Includes a property that returns the volatility (standard deviation of returns).
    '''

    def __init__(self, name, prices):
        self.name = name
        self.prices = prices
        self.returns = self.calc_returns()

    def calc_returns(self, prices=None):
        if prices == None:
            prices = self.prices
        returns = [prices[i]/prices[i-1] for i in range(1, len(prices))]
        return returns

    def calc_mean(self, source=None):
        if source == None:
            source = self.prices
        from statistics import mean
        return mean(source)

    def calc_median(self, source=None):
        if source == None:
            source = self.prices
        from statistics import median
        return median(source)

    def calc_stdev(self, source=None):
        if source == None:
            source = self.prices
        from statistics import stdev
        return stdev(source)

    @property
    def volatility(self):
        return self.calc_stdev(self.returns)

        
tsla_prices = [123.4, 124.4, 123.3, 142.2, 122.2, 143.1, 124.4, 123.3, 142.2, 123.3, 142.2, 122.2, 143.1, 142.2, 122.2, 143.1, 124.4, 123.3, 142.2, 123.3, 124.4,]
x = StockAnalyzer("TSLA", tsla_prices)

print(f"Name: {x.name}")
print(f"Prices: {x.prices}")
print(f"Returns: {x.returns}")
print(f"Mean: {x.calc_mean()}")
print(f"Median: {x.calc_median()}")
print(f"Standard deviation: {x.calc_stdev()}")
print(f"Volatility: {x.volatility}")