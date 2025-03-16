# stocks = [
#     ("AAPL", 170.25, "Technology"),
#     ("XOM", 112.80, "Energy"),
#     ("JPM", 145.50, "Financial"),
#     ("AMZN", 128.90, "Technology"),
#     ("JNJ", 152.60, "Healthcare")
# ]

# # Write list comprehensions to:
# # 1. Extract all technology stocks
# # 2. Get just the symbols of stocks over $150
# # 3. Calculate a 5% increase on all prices

# tech_stocks = [symbol for symbol, price, sector in stocks if sector == "Technology"]
# over_150 = [symbol for symbol, price, sector in stocks if price > 150]
# pc5 = [(symbol, price * 1.05, sector) for symbol, price, sector in stocks]
###################################
###################################
# Write a function that creates a new portfolio with only profitable positions
# Returns a new list without modifying the original

positions = [
    ("AAPL", 170.25, "Technology"),
    ("XOM", 112.80, "Energy"),
    ("JPM", 145.50, "Financial"),
    ("AMZN", 128.90, "Technology"),
    ("JNJ", 152.60, "Healthcare")
]

current_prices = {
    "AAPL": 172.25,
    "XOM": 110.80,
    "JPM": 146.50,
    "AMZN": 129.90,
    "JNJ": 150.60,
}

def filter_profitable_positions(positions, current_prices):
    """
    positions: List of (symbol, purchase_price, shares)
    current_prices: Dict mapping symbols to current prices
    Returns: New list with only positions where current_price > purchase_price
    """
    return [stock for stock, purchase_price, sector in positions if purchase_price < current_prices[stock]]

profitable = filter_profitable_positions(positions, current_prices)

