# Store positions with (symbol, entry_date) as keys
# Allow adding new positions
# Calculate the current value and P&L of the portfolio

def portfolio_manager(positions=None):
    """
    Create a portfolio management system using dictionaries.
    
    Args:
        positions (dict, optional): Initial positions with (symbol, date) keys
    
    Returns:
        dict: A dictionary with portfolio management functions
    """
    # Initialize the portfolio if none is provided
    if positions is None:
        positions = {}
    
    # Portfolio management functions
    def add_position(symbol, entry_date, shares, entry_price):
        """Add a new position to the portfolio."""
        nonlocal positions
        positions.update({
            (symbol, entry_date): {"shares": shares, "entry_price": entry_price}
        })
        
    def calculate_value(current_prices):
        """
        Calculate the current portfolio value and P&L.
        
        Args:
            current_prices (dict): Dictionary with symbols as keys and current prices as values
            
        Returns:
            dict: Current value, cost basis, and overall P&L
        """
        nonlocal positions

        return sum([current_prices[key[0]] * data["shares"] for key, data in positions.items()])

    
    # Return functions in a dictionary
    return {
        "positions": positions,
        "add_position": add_position,
        "calculate_value": calculate_value
    }

# Example usage (to help guide your implementation):
portfolio = portfolio_manager()
portfolio["add_position"]("AAPL", "2025-03-10", 10, 178.25)
portfolio["add_position"]("MSFT", "2025-03-15", 5, 325.50)
current_prices = {"AAPL": 182.50, "MSFT": 330.25}
portfolio_value = portfolio["calculate_value"](current_prices)

print(portfolio_value)