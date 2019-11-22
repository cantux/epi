import copy

def combs(arr, choose):
    len_arr = len(arr)
    ret = []
    def rec(start, count, sub):
        if count == choose:
            ret.append(copy.deepcopy(sub))
            return
        for i in range(start, len_arr):
            sub.append(arr[i])
            rec(i + 1, count + 1, sub)
            sub.pop()

    rec(0, 0, [])
    print ret
    return []

def test():
    assert combs(range(3), 2) == []

if __name__ == "__main__":
    test()
