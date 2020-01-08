
def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    len_r = len(grid)
    len_c = len(grid[0])
    
    dp = [[0 for _ in range(len_c)] for _ in range(len_r)]
    dp[0][0] = grid[0][0]
    for i in range(1, len_c):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
        
    for i in range(1, len_r):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        
    for r in range(1, len_r):
        for c in range(1, len_c):
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
            
    return dp[len_r - 1][len_c - 1]
