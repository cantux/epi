
#!/usr/bin/env python

def opt_r(arr):
    len_arr = len(arr)
    dp = [[-sys.maxint - 1 for _ in len_arr] for _ in len_arr]
    def rec(i, j):
        if i >= j:
            return 0
        if dp[i][j] != -sys.maxint - 1:
            return dp[i][j]

        dp[i][j] = max( \
                min(rec(i + 1, j - 1), rec(i + 2, j)) + arr[i], 
                min(rec(i, j - 2), rec(i + 1, j - 1))+ arr[i]
                )

        return dp[i][j]

    return rec(0, len_arr)

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

