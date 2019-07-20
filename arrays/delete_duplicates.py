def rem_dupsa(a):
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

def rem_dups(arr):
    if len(arr) == 1: return arr

    curr, last_valid = 1, 1
    last = arr[0]
    while curr < len(arr):
        if arr[curr] != last:
            arr[last_valid] = arr[curr] 
            last_valid += 1
            last = arr[curr]
        curr += 1
    print arr[0: last_valid]
    return arr[0: last_valid]

def test():
    assert rem_dups([1, 1, 2, 2 ,3 ,3]) == [1, 2, 3]
    assert rem_dups([1, 1, 2, 2 ,3 ,3, 4]) == [1, 2, 3, 4]
    assert rem_dups([1, 1, 2, 2 ,3 ,3, 5, 5, 5, 5]) == [1, 2, 3, 5]
    assert rem_dups([1, 2, 3]) == [1, 2, 3]

if __name__ == "__main__":
    test()

