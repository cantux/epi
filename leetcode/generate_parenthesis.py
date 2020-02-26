    dp = [[] for i in range(n + 1)]
    dp[0].append('')
    for i in range(n + 1):
	for j in range(i):
	    dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
    return dp[n]

from functools import lru_cache
from itertools import product
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        @lru_cache(None)
        def recur(n=n):
            if n == 0:
                return [""]
            ans = []
            for i in range(n):
                for a, b in product(recur(i), recur(n - 1 - i)):
                    #ans.append(f"({a}){b}")
                    ans.append(f"({b}){a}") # match the sample order
            return ans
        return recur(n) 
