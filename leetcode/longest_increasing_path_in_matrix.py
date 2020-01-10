    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        len_r = len(matrix)
        len_c = len(matrix[0])
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dp = [[0 for _ in range(len_c)] for _ in range(len_r)]
        
        def check_boundry(r, c):
            return r < len_r and r >= 0 and c < len_c and c >= 0
        
        def dfs_memo(curr_r, curr_c):
            if dp[curr_r][curr_c] == 0:
                max_found = 0
                for r,c in directions:
                    new_r, new_c = curr_r + r, curr_c + c                            
                    if check_boundry(new_r, new_c):
                        if matrix[new_r][new_c] > matrix[curr_r][curr_c]:
                            max_found = max(max_found, dfs_memo(new_r, new_c) + 1)                        
                dp[curr_r][curr_c] = max_found
            return dp[curr_r][curr_c]
        
        glob_max = 0
        for r in range(len_r):
            for c in range(len_c):
                glob_max = max(glob_max, dfs_memo(r, c))
                
        return glob_max
