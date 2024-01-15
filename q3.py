def maxProf(prices):
    if len(prices) == 0:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(prices[i] - min_price, max_profit)

    return max_profit


arr = [7, 6, 4, 3, 1]
print(maxProf(arr))
