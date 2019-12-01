#!/usr/bin/env python

def LCS(sq1, sq2):
    # instead of trying to find the longest sequence fing the length of the longest sequence.
    # let's imagine at a given subproblem I am able to find the next subproblem 
    # subproblem: given position at sq1 i
    #             position at sq2 j
    #             if sq2[i] == sq2[j] then we know we have less subproblems.
    # how do we know if the prefix solution, considering less characters yield to a solution?
    # 
    # guess: where is the next matching character? This is not enough. We also need to be looking for the 
    len_sq1 = len(sq1)
    len_sq2 = len(sq2)
    dp = [[0 for _ in range(len_sq2)] for _ in range(len_sq1)]
    sol = []
    for i in xrange(1, len_sq1):
        for j in xrange(1, len_sq2):
            if sq1[i] == sq2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                sol.append((1, 1))
            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                sol.append((1, 0))
            else:
                dp[i][j] = dp[i][j - 1]
                sol.append((0, 1))

    sq1_ptr = 0
    ret = ""
    for sq1_move, sq2_move in sol[::-1]:
        if sq1_move == 1:
            ret += sq1[sq1_ptr]
            sq1_ptr += 1
        else:
            sq1_ptr += 1

    print ret


    print c
    return []

def test():

    assert LCS("abc", "aabbcc") == "abc"
    assert LCS("abc", "abc") == "abc"
    assert LCS("aab", "ab") == "ab"
    assert LCS("abc", "ab") == "ab"
    assert LCS("aab", "aaabb") == "aab"
    assert LCS("abc", "bca") in ["a", "b", "c"]

if __name__ == "__main__":
    test()

