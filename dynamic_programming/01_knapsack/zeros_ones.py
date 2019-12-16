def brut(strs, m, n):
    len_s = len(strs)
    lst = [] # list of tuples
    for s in strs:
        zero_c = 0
        one_c = 0
        for c in s:
            if c == "0":
                zero_c += 1
            else:
                one_c += 1
            lst.append((zero_c, one_c))
    
    def rec(curr_idx, rem_m, rem_n):
        if curr_idx == len_s: # m = 0, n = 0
            return 0
        using_curr = 0 
        if rem_m >= lst[curr_idx][0] and rem_n >= lst[curr_idx][1]:
            using_curr = 1 + rec(curr_idx + 1, rem_m - lst[curr_idx][0], rem_n - lst[curr_idx][1])
        return max(using_curr, rec(curr_idx + 1, rem_m, rem_n))
    return rec(0, m, n)

def memo(strs, m, n):
    memo = {}
    def findMax(strs, i, m, n):
	if i <= len(strs)-1:
	    if (i, m, n) in memo:
		return memo[(i,m,n)]
	    
	    if m > 0 or n > 0:
		# use it or skip it
		m1 = strs[i].count('0')
		n1 = strs[i].count('1')
		use = 0
		
		skip = findMax(strs, i+1, m, n)
		
		if m1 <= m and n1 <= n:
		    use = findMax(strs, i+1, m-m1, n-n1) + 1
		
		counter = max(use, skip)
		memo[(i,m,n)] = counter
		
		return memo[(i,m,n)]
	
	return 0
	
    counter = findMax(strs, 0, m, n)
    return counter

def tab(strs, m, n):
    length = len(strs)
    dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(length+1)]
                
    for i in range(1, length+1):
        s = strs[i-1]
        m1 = s.count('0')
        n1 = s.count('1')
        
        for j in range(m+1):
            for k in range(n+1):
                # this string can be used, so choose to use or skip
                if j >= m1 and k >= n1:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-m1][k-n1]+1)
                
                # definitely cannot use this string
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    
    return dp[-1][-1][-1]

def tab_opt(strs, m, n):
    length = len(strs)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
      
    for s in strs:
        m1, n1 = 0, 0
        for ch in s:
            if ch == '0':
                m1 += 1
            else:
                n1 += 1
        
        for j in range(m, m1-1, -1):
            for k in range(n, n1-1, -1):
                # can be used, so choose to use or skip
                if j >= m1 and k >= n1:
                    dp[j][k] = max(dp[j][k], dp[j-m1][k-n1]+1)
    
    return dp[-1][-1] 

def test():
    assert brut(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert brut(["10", "0", "1"], 1, 1) == 2
    assert memo(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert memo(["10", "0", "1"], 1, 1) == 2
    assert tab(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert tab(["10", "0", "1"], 1, 1) == 2
    assert tab_opt(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert tab_opt(["10", "0", "1"], 1, 1) == 2


if __name__ == "__main__":
    test()
