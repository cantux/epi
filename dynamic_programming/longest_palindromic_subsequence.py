
import pprint

def lps(s):
    len_s = len(s)

    dp = [[0 for _ in range(len_s)] for _ in range(len_s)]
    for i in range(len_s):
        dp[i][i] = 1

    for sub_len in range(1, len_s):
        for i in range(len_s - sub_len):
            for j in range(i + sub_len, len_s):
#                 print "i: ", i, " j: ", j
#                 print "chars: si: ", s[i], " sj: ", s[j]
#                 print "dp[i][j]: ", dp[i][j]
#                 print "dp[i + 1][j - 1]: ", dp[i + 1][j - 1]
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
#             pprint.pprint(dp) 

#     pprint.pprint(dp)
    return dp[0][len_s - 1]

def test():
    assert lps("bbbab") == 4
    # also construct the solution.


if __name__ == "__main__":
    test()
