#!/usr/bin/env python

import sys

def fnc(matrices):
    num_matrices = len(matrices)
    p = [0] * (num_matrices + 1)
    p[0] = matrices[0][0]
    for i in xrange(1, len(matrices) + 1):
        p[i] = matrices[i - 1][1]
    
    print p
    dp = [[0 for _ in xrange(num_matrices)] for _ in xrange(num_matrices)]
    print dp
    for i in range(1, num_matrices):
        dp[i][i] = 0
    print "dp: ", dp

    s = [[None for _ in xrange(num_matrices)] for _ in xrange(num_matrices)]
    print "s: ", s 
    for chain_length in xrange(2, num_matrices):
        for i in xrange(1, num_matrices - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = sys.maxint
            for k in xrange(i, j):
                curr = dp[i][k] + dp[k+1][j] + p[i - 1] * p[k] * p[j]# (matrices[i][1] * matrices[k][1] * matrices[j][1])
                if curr < dp[i][j]:
                   dp[i][j] = curr
                   s[i][j] = k
    
    print "s:", s
    print "dp: ", dp
    return dp[1][num_matrices - 1]

def test():
    matrices = [(10, 100), (100, 5), (5, 50)]
    assert fnc(matrices) == 7500

if __name__ == "__main__":
    test()

