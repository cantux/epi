#!/usr/bin/env python

def lcs(s1, s2):
    lcs_length = tab_opt(s1, s2)
    return len(s1) + len(s2) - lcs_length

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
    assert lcs("abcf", "bdcf") == 5
    assert lcs("dynamic", "programming") == 15


if __name__ == "__main__":
    test()

