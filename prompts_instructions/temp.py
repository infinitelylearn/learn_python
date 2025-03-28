class Portfolio:
    def __init__(self, positions=None):
        print("here")
        print(positions)
        self.positions = positions or {}  # Dict of symbol -> shares
        print(positions)
        print("here")
        
    def __getitem__(self, symbol):
        # Called when you use portfolio["AAPL"]
        return self.positions.get(symbol, 0)
        
    def __setitem__(self, symbol, shares):
        # Called when you use portfolio["AAPL"] = 10
        self.positions[symbol] = shares
        
    def __delitem__(self, symbol):
        # Called when you use del portfolio["AAPL"]
        if symbol in self.positions:
            del self.positions[symbol]
            
    def __len__(self):
        # Called when you use len(portfolio)
        return len(self.positions)
        
    def __contains__(self, symbol):
        # Called when you use "AAPL" in portfolio
        return symbol in self.positions

# Using our Portfolio class with collection-like behaviors
portfolio = Portfolio()

# Accessing positions
print(portfolio["AAPL"])   # 10

# Adding a new position
portfolio["GOOG"] = 3
print(portfolio["GOOG"])   # 3

# Checking if a symbol exists
print("AAPL" in portfolio)  # True
print("TSLA" in portfolio)  # False

# Getting the number of positions
print(len(portfolio))       # 3

# Removing a position
del portfolio["MSFT"]
print(len(portfolio))       # 2