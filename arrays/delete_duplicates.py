def rem_dups(a):
    last = a[0]
    swap_dist = 0
    i = 1
    while i < len(a):
        if last == a[i]:
            swap_dist += 1
        else:
            last = a[i]
            a[i], a[i - swap_dist] = 0, a[i]
        i += 1
    return a[0:len(a) - swap_dist]

def test():
    assert rem_dups([1, 1, 2, 2 ,3 ,3]) == [1, 2, 3]
    assert rem_dups([1, 1, 2, 2 ,3 ,3, 4]) == [1, 2, 3, 4]
    assert rem_dups([1, 1, 2, 2 ,3 ,3, 5, 5, 5, 5]) == [1, 2, 3, 5]
    assert rem_dups([1, 2, 3]) == [1, 2, 3]

if __name__ == "__main__":
    test()

