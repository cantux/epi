rcleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set()
        def dfs(curr):
            if curr in seen:
                return
            seen.add(curr)
            
            for i, s in enumerate(M[curr]):
                if s == 1:
                    dfs(i)
        
        res = 0
        for m in range(len(M)):
            if m not in seen:
                dfs(m)
                res += 1
                
        return res
            
