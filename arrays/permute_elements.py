def permute(arr):
    len_a = len(arr)
    res = []
    def directed_permutations(curr):
        if curr == len_a - 1:
            res.append(arr[:])
            return

        for i in range(curr, len_a):
            arr[curr], arr[i] = arr[i], arr[curr]
            directed_permutations(curr + 1)
            arr[curr], arr[i] = arr[i], arr[curr]

    directed_permutations(0)
    return res

# given an array of n elements and a permutation P, apply P to A
def apply_permutation(arr, perm):
    # every permutation can be represented by a collection of independent permutations
    # each of which is cyclic.
    # it moves elememnts by a fixed offset wrapping around
    # we want to find disjoint cycles that constitute the permutation.

    # trick is to mark the permutation array as we go along swapping elements.
    len_a = len(arr)
    for i in range(len_a):
        nxt = i
        while perm[nxt] >= 0:
            arr[i], arr[perm[nxt]] = arr[perm[nxt]], arr[i]
            temp = perm[nxt]
            perm[nxt] -= len(perm)
            nxt = temp
    # restore permutation array
    perm[:] = [a + len_perm for a in perm]
    

def next_permutation(arr):
# find first non-decreasing suffix, assume it starts at kth index
# find the first element that is larger than arr[k] between k+1, assume it is at index l
# swap arr[l] and arr[k]
# reverse the sequence after index k + 1
    len_a = len(arr)
    k = len_a - 2
    while k >= 0 and arr[k] >= arr[k + 1]:
        k -= 1
    if k == -1:
        return reversed(arr)
    for i in reversed(range(k + 1, len_a)):
        if arr[i] > arr[k]:
            arr[k], arr[i] = arr[i], arr[k]
            break
    arr[k + 1:] = reversed(arr[k + 1:])
    return arr


def test():
    res = permute([1, 2, 3])
    t_list = []
    map(lambda x: t_list.append(x in [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]), res)
    assert all(t_list)

    apply_permutation([4, 5, 6], [3, 2, 1]) == [6, 5, 4]

if __name__ == "__main__":
    test()
