    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r_l = len(grid)
        if not r_l: return 0
        c_l = len(grid[0])
        
        def dfs(row, col):
            if 0 <= row < r_l and 0 <=col < c_l:
                if grid[row][col] == "1":
                    grid[row][col] = 0
                    dfs(row, col + 1)
                    dfs(row + 1, col)
                    dfs(row - 1, col)
                    dfs(row, col - 1)
            
        
        count = 0
        for r in range(r_l):
            for c in range(c_l):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
                
        return count
        
