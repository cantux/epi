
#!/usr/bin/env python

# Given a circular array (the next element of the last element is the first element of the array), 
# print the Next Greater Number for every element. 
# The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number.

def nge_brut(arr):
    # 1, 2, 3, 4 -> 2, 3, 4, -1
    # 4, 3, 2, 1 -> -1, 4, 4, 4
    # if any element is larger than the current one
    # then set it to the result on previous element's index
    # if none of the elements are lareger than the current one until the end, we have to start looking from the beginninbg
    
    # brute force
    len_n = len(arr)
    res = []
    for i in range(len_n):
        found = False
        for j in range(i + 1, len_n + i):
            if arr[j % len_n] > arr[i]:
                res.append(arr[j % len_n])
                found = True
                break
        if not found:
            res.append(-1)
    return res

def nge(nums):
    len_n = len(nums)
    res = [-1] * len_n
    s = []

    for i in range(len_n * 2):
        while s and nums[s[-1]] < nums[i % len_n]:
            curr = s.pop()
            res[curr] = nums[i % len_n]
        s.append(i % len_n)
    return res

def test():
    assert nge_brut([1, 2, 1]) == [2, -1, 2]
    assert nge_brut([3, 8, 4, 1, 2]) == [8, -1, 8, 2, 3]

    assert nge([1, 2, 1]) == [2, -1, 2]
    assert nge([3, 8, 4, 1, 2]) == [8, -1, 8, 2, 3]


if __name__ == "__main__":
    test()

