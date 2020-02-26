# this is 40ms
def word_break(s, wordDict):
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

# this is 140ms
# see that heuristic is getting really important here.
def wordBreak(self, s, wordDict):
    len_s = len(s)
    suffix_memo = [-1] * (len_s + 1)
    suffix_memo[len_s] = True
    
    def rec(start):
        if suffix_memo[start] == -1:
            suffix_memo[start] = False
            for i in range(start, len_s + 1):
                curr_cut = s[start : i]
                print "trying for: ", curr_cut
                if curr_cut in wordDict:
                    if rec(i):
                        suffix_memo[start] = True
                        break
            
        return suffix_memo[start]
        
    return rec(0)
