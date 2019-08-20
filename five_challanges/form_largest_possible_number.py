import heapq

def largest(nums):
    quickSort(nums, 0, len(nums)-1)
    return str(int("".join(map(str, nums)))) 

def quickSort(nums, l, r):
    if l >= r:
        return 
    pos = partition(nums, l, r)
    quickSort(nums, l, pos-1)
    quickSort(nums, pos+1, r)
    
def partition(nums, l, r):
    low = l
    while l < r:
        if compare(nums[l], nums[r]):
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low


def compare(n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

def test():
    assert largest([50, 2, 1, 9]) == '95021'

    assert largest([0]) == '0'

if __name__ == "__main__":
    test()
