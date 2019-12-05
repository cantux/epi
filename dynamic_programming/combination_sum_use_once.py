# trick about this question is that it contains duplicates in the array
# so (1 1 6) is a solution, while (7 1) is not if (1 7) was encountered before.
# we can either check when we insert to the solution set
# or we can sort the list, add everything, then convert solution to a set.

# I am more interested in finding the subproblem definition rather than constructing a solution.

def brut(candidates, target):
    len_c = len(candidates)
    def rec(curr_idx, rem):
        if rem == 0:
            return 1
        elif curr_idx == len_c or rem < 0:
            return 0
        used = 0
        if rem >= candidates[curr_idx]:
            used = rec(curr_idx + 1, rem - candidates[curr_idx])
        return used + rec(curr_idx + 1, rem)

    return rec(0, target)

def memo(candidates, target):
    len_c = len(candidates)
    dp = [[-1] * (target + 1) for _ in range(len_c)]
    def rec(curr_idx, rem):
        if rem == 0:
            return 1
        elif curr_idx == len_c or rem < 0:
            return 0
        if dp[curr_idx][rem] == -1:
            used = 0
            if rem >= candidates[curr_idx]:
                used = rec(curr_idx + 1, rem - candidates[curr_idx])
            dp[curr_idx][rem] = rec(curr_idx + 1, rem) + used
        return dp[curr_idx][rem]

    return rec(0, target)

# see subtle differences to memoization: 
# 1) we need to look back at a previous candidate, so we increase the candidate dimension by 1. 
# 2) initialize our lookup table with 1s # covering cases remaining is equal to the candidate(t - c = 0)
def tab(candidates, target):
    len_c = len(candidates)
    dp = [[0] * (target + 1) for _ in range(len_c + 1)]

    for i in range(len_c + 1):
        dp[i][0] = 1

    for c_i, c in enumerate(candidates):
        for t in range(1, target + 1):
            used = 0
            if t >= c:
                used = dp[c_i][t - c]
            dp[c_i + 1][t] = dp[c_i][t] + used
    return dp[len_c][target]

# space optimization here is a bit tricky.
# we are exploiting the fact that if we traverse reverse, subproblems don't get overriden
def tab_opt(candidates, target):
    len_c = len(candidates)

    dp = [1] + [0] * target

    for c in candidates:
        for t in xrange(target, c - 1, -1):
            dp[t] += dp[t - c]
    return dp[target]

def test():
    assert brut([10,1,2,7,6,1,5], 8) == 6
    assert brut([2,5,2,1,2], 5) == 4
    assert memo([10,1,2,7,6,1,5], 8) == 6
    assert memo([2,5,2,1,2], 5) == 4
    assert tab([10,1,2,7,6,1,5], 8) == 6
    assert tab([2,5,2,1,2], 5) == 4
    assert tab_opt([10,1,2,7,6,1,5], 8) == 6
    assert tab_opt([2,5,2,1,2], 5) == 4


if __name__ == "__main__":
    test()
