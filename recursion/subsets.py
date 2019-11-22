import copy

def subsets(arr):
    len_arr = len(arr)
    ret = []
    count = [0]
    def rec(start, par):
        count[0] += 1
        ret.append(copy.deepcopy(par))
        for i in range(start, len_arr):
            par.append(arr[i])
            rec(i + 1, par)
            par.pop()

    rec(0, [])
    print count[0]
    print ret
    return count

def test():
    assert subsets(range(3)) == 8

if __name__ == "__main__":
    test()
