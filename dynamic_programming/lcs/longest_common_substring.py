
#!/usr/bin/env python

# given two strings find the length of the longest common substring
# 
def brut(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    def rec(i, j, count):
        if i == len_s1 or j == len_s2:
            return count
        if s1[i] == s2[j]:
             return rec(i + 1, j + 1, count + 1) 
        return max(count, rec(i + 1, j, 0), rec(i, j + 1, 0))

    return rec(0, 0, 0)

def tab(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)

    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    max_found = 0
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_found = max(max_found, dp[i][j])
    return max_found
    
def tab_opt(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(2)]
    max_found = 0

    for i in range(len_s1):
        for j in range(len_s2):
            dp[i % 2][j] = 0
            if s1[i] == s2[j]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                max_found = max(max_found, dp[i % 2][j])

    return max_found

def test():
    assert brut("abdca", "cbda") == 2
    assert brut("passport", "ppsspt") == 3

    assert tab("abdca", "cbda") == 2
    assert tab("passport", "ppsspt") == 3

    assert tab_opt("abdca", "cbda") == 2
    assert tab_opt("passport", "ppsspt") == 3



if __name__ == "__main__":
    test()

