        if not wordDict: return False
        len_s = len(s)
        memo = [-1] * len_s
        max_len = max(map(len, wordDict))
        def rec(start):
            if start == len_s:
                return True
            if memo[start] == -1:
                for i in range(start, start + max_len + 1):
                    if s[start:i+1] in wordDict and rec(i + 1):
                        memo[start] = True
                        return True
                memo[start] = False
            return memo[start]
        
        return rec(0)
