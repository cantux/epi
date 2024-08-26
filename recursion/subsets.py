import copy
import itertools

def subsets(arr):
    len_arr = len(arr)
    res = []
    count = [0]
    def helper(curr_idx, curr_lst):
        if curr_idx == len_arr:
            count[0] += 1
            res.append(curr_lst[:])
            return

        helper(curr_idx + 1, curr_lst)
        helper(curr_idx + 1, curr_lst + [arr[curr_idx]])

    helper(0, [])
    print(count[0])
    print(res)
    return res

def powerset(n):
    res = []
    count = [0]
    def helper(curr_idx, curr_lst):
        count[0] += 1
        res.append(curr_lst[:]) 
        for i in range(curr_idx, n):
            curr_lst.append(i)
            helper(i + 1, curr_lst)
            curr_lst.pop()

    helper(0, [])
    print(count[0])
    print(res)
    return res

def test():
    ps = powerset(3)
    ss = subsets(range(3))
    assert all(s in ps for s in ss)

if __name__ == "__main__":
    test()
