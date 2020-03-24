
#!/usr/bin/env python

# given two strings find the length of the longest common subsequence
# 
def brut(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    def rec(i,j):
        if i == len_s1 or j == len_s2:
            return 0
        
        if s1[i] == s2[j]:
            return rec(i + 1, j + 1) + 1
        return max(rec(i + 1, j), rec(i, j + 1))

    return rec(0,0)

def memo(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)

    dp = {}
    def rec(i,j):
        key = str(i) + "_" + str(j)
        if key not in dp:
            if i == len_s1 or j == len_s2:
                return 0
            
            if s1[i] == s2[j]:
                res = rec(i + 1, j + 1) + 1
            else:
                res = max(rec(i + 1, j), rec(i, j + 1))
            dp[key] = res
        return dp[key]

    return rec(0,0)

def tab(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len_s1][len_s2]

def tab_opt(s1, s2):
  len_s1, len_s2 = len(s1), len(s2)
  dp = [[0 for _ in range(len_s2 + 1)] for _ in range(2)]
  max_found = 0
  for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
      if s1[i - 1] == s2[j - 1]:
        dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
      else:
        dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

      max_found = max(max_found, dp[i % 2][j])

  return max_found

def test():
    assert brut("abdca", "cbda") == 3
    assert brut("passport", "ppsspt") == 5
    assert memo("abdca", "cbda") == 3
    assert memo("passport", "ppsspt") == 5
    assert tab("abdca", "cbda") == 3
    assert tab("passport", "ppsspt") == 5
    assert tab_opt("abdca", "cbda") == 3
    assert tab_opt("passport", "ppsspt") == 5


if __name__ == "__main__":
    test()

