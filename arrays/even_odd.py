# given an array reorder entries so that the even comes first

# brute force
# create a buffer to keep the evens and odds.
# complexity will be O(n) Space will be O(n)
# can I do this in-place and without two passes?
# keep an evens and odds at both ends and keep track of their indices
# keep the odds at the end and keep a current
# do I keep the order? if I should, I ain't going to swap, if I sohuldn't I can halve the time.
def even_first_order(arr):
    curr = 0
    odd_ptr = len(arr) - 1

    while curr < odd_ptr:
        if arr[curr] % 2 == 0:
            curr += 1
        else:
            arr[curr], arr[odd_ptr] = arr[odd_ptr], arr[curr]
#             temp = arr[curr]
#             arr[curr] = arr[odd_ptr] 
#             arr[odd_ptr] = temp
            odd_ptr -= 1
    return arr

# now let's write some tests
# 
def test():
    arr = [1, 2, 3, 4, 5]
    print even_first_order(arr)
    print even_first_order(arr)
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print even_first_order(arr)

    arr = [5, 4, 3, 2, 1]
    print even_first_order(arr)

if __name__ == "__main__":
    test()
