
#!/usr/bin/env python

import itertools

def perms(lst):
    res = []
    len_l = len(lst)

    def helper(curr):
        if curr == len_l:
            res.append(tuple(lst[:]))
            return
        for i in range(curr, len_l):
            lst[curr], lst[i] = lst[i], lst[curr]
            helper(curr + 1)
            lst[curr], lst[i] = lst[i], lst[curr]

    helper(0)
    return res

def test():
    case_1 = list(range(3))
    cases = [
            case_1
            ]
    for case in cases:
        python_perms = list(itertools.permutations(case))
        results = perms(case)
        assert all(res in python_perms for res in results) and (len(python_perms) == len(results))

if __name__ == "__main__":
    test()

