"""This function gives max profit by buying and selling stocks"""
from typing import List


def stock_max_profit(prices: List[int]) -> int:
    """
    Find maximum profit from a single buy and sell transaction.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


if __name__ == "__main__":
    stocks_data = [7, 1, 5, 3, 6, 4]
    print(stock_max_profit(stocks_data))
