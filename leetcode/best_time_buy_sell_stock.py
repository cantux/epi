
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

def dp(prices):
    if len(prices) == 0:
        return 0
    dp = [0] * len(prices)
    cur_min = prices[0]
    for i in range(len(prices)):
        if prices[i] <= cur_min:
            dp[i] = 0
            cur_min = prices[i]
        else:
            dp[i] = max(prices[i]-cur_min, 0)
    return max(dp)

def dp_o1(prices):
    len_p = len(prices)
    if len_p < 2: return 0
    min_so_far = prices[0]
    max_profit = -sys.maxsize - 1
    for i in range(1, len_p):
        min_so_far = min(min_so_far, prices[i])
        max_profit = max(max_profit, prices[i] - min_so_far)
        
    return max_profit
def test():
    assert dp([7,1,5,3,6,4]) == 5
