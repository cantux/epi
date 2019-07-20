# record maximum profit and the indeces that made it

import sys

def bs(arr):
    max_profit, min_price_so_far = -sys.maxint - 1, sys.maxint
    for i, el in enumerate(arr):
        max_profit_sell_today = el - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, el)
    return max_profit

def test():
    assert bs([100, 90, 50, 60, 40, 100]) == 60
    assert bs([100, 90]) == 0
    assert bs([90, 100]) == 10
    assert bs([90, 100, 120]) == 30

if __name__ == "__main__":
    test()
