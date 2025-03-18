def calculate_rsi(prices, period=14):
    """
    Calculate the Relative Strength Index for a list of prices.
    
    Args:
        prices (list): List of closing prices
        period (int): RSI period, default is 14
        
    Returns:
        float: The RSI value for the given period
    """

    # length validation
    if len(prices) > period:
        print("More price data required")
        return []

    price_changes = [prices[i] - prices[i-1] / prices[i-1] * 100 for i in range(1, len(prices)) + 1 ]
    
    # Your implementation here
    # 1. Calculate price changes
    # 2. Separate gains and losses
    # 3. Calculate average gain and average loss
    # 4. Calculate RS (Relative Strength)
    # 5. Calculate RSI = 100 - (100 / (1 + RS))
    pass