
# # 
# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
# 
# For example, given the array arr = [7, 1, 3, 2, 4, 5, 6] we perform the following steps:
# 
# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took  swaps to sort the array.

def minimumSwaps(arr):
    # okay, instead of speculating on a solution here let's try to construct one
    
    # brute force
    # decision problem,
    # which value to swap first with the current index could make this array sorted
    len_a = len(arr)
    res = 0
    for i in range(len_a):
        nxt = i
        cycle_size = 0
        while arr[nxt] > 0:
            temp = arr[nxt] - 1
            arr[nxt] -= len_a
            nxt = temp
            cycle_size += 1
        if cycle_size > 0:
            res += cycle_size - 1
    return res
