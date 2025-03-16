prices = [105.42, 107.31, 106.98, 108.41, 109.73, 108.25]

for i in range(2, len(prices)):
    if prices[i] > prices[i-1] and prices[i-1] > prices[i-2]:
        print("Bullish")
    elif prices[i] < prices[i-1] and prices[i-1] < prices[i-2]:
        print("Bearish")