def fnc(arr):
    for i, a in enumerate(arr):
        arr[i] = (a, i)

    arr.sort(key=lambda x: x[0])

    ret = [None] * len(arr)

    for i, (v, p) in enumerate(arr):
        ret[p] = i + 1

    return ret

    

def test():
#     assert fnc([]) == []
    assert fnc([10, 8, 15, 12, 6, 20, 1]) == [4, 3, 6, 5, 2, 7, 1]

if __name__ == "__main__": 
    test()
