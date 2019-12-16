# given a non negative integer number num
# For every numr i in range 0 <= i <= num, find the number of 1s
# trick is to see that we will already be calculating the 1 bit shifted result
# and just adding either 1 or 0 based on the LSB
count_bits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """
    if num == 0: return [0]
    dp = [0] * (num + 1)
    dp[1] = 1
    for i in range(2, num + 1):
        curr = i & 1
        lookup = i >> 1
        dp[i] = dp[lookup] + curr
    return dp     
