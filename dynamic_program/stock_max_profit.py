"""This function gives max profit by buying and selling stocks"""


def stock_max_profit():
    """
    max profit by buying and selling stocks
    """
    stocks_data = [7, 1, 5, 3, 6, 4]
    mini = stocks_data[0]
    max_profit = 0
    for i in stocks_data:
        profit = i - mini
        max_profit = max(max_profit, profit)
        mini = min(i, mini)
    return max_profit


print(stock_max_profit())
