import copy

def backtrack(candidates, target):
    len_c = len(candidates)
    
    pi = []
    def rec(curr_idx, rem, d):
        if rem == 0:
            pi.append(copy.deepcopy(d))
            return True
        if rem < 0 or curr_idx >= len_c:
            return False
        
        
        d.append(candidates[curr_idx])
        rec(curr_idx, rem - candidates[curr_idx], d)
        d.pop()
        rec(curr_idx + 1, rem, d)
            
    rec(0, target, [])
    return pi

def tab(candidates, target):
    candidates.sort()
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    
    pi = {i: [] for i in range(target + 1)}
    pi[0] = [[]]
    
    for c in candidates:
        for t in range(c, target + 1): # use the check if c <= t: if you start range from 1
            prev_val = dp[t - c]
            dp[t] += prev_val
            if prev_val != 0:
                for p in pi[t - c]:
                    prev_l = copy.deepcopy(p)
                    prev_l.append(c)
                    pi[t].append(prev_l)

    return pi[target]

def tab_opt(candidates, target):
    pi = {i: [] for i in range(target + 1)} #  defaultdict(list)
    pi[0] = [[]]
    
    for c in candidates:
        for t in range(c, target + 1): # use the check if c <= t: if you start range from 1
            if pi[t - c]:
                for p in pi[t - c]:
                    prev_l = p[:]
                    prev_l.append(c)
                    pi[t].append(prev_l)

    return pi[target]

def test():
    assert all([i in [[2, 2, 3], [2, 5]] for i in tab([2, 3, 5], 7)])


if __name__ == "__main__":
    test()
