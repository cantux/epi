
def maxProfit(p):
    """
    :type prices: List[int]
    :rtype: int
    """
    # brute force n^2
    len_p = len(p)
    max_profit = 0
    for i in range(len_p):
        for j in range(i, len_p):
            max_profit = max(max_profit, p[j] - p[i])
    return max_profit

def dp(p):
   pass

def test():
    assert dp([7,1,5,3,6,4]) == 5
