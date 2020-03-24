def getMoneyAmount(self, n):
    """
    :type n: int
    :rtype: int
    """
    memo = {}
    def rec(start, end):
	if start >= end:
	    return 0
	key = str(start) + "_" + str(end)
	if key not in memo:
	    min_found = sys.maxsize
	    for i in range(start, end + 1):
		min_found = min(min_found, max(rec(start, i - 1), rec(i + 1, end)) + i)
	    memo[key] = min_found
	return memo[key]
    
    return rec(1, n)
