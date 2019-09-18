

import heapq

# decomp
# euclidian: x - 0 ^2 + y - 0 ^2 ^ 1/2
def k_closest(points, K):
    if K == 0 or not points:
        return []

    h = []
    for x, y in points:
        val = ((x ** 2) + (y ** 2)) # no need for the following ** (0.5)
        if not h or h[0] > val * -1:
            heapq.heappush(h, (val * -1, (x, y)))
        if len(h) > K:
            heapq.heappop(h)

    return [heapq.heappop(h)[1] for _ in range(len(h))]

def quick_select(lst, k, small, big, pivot):
    
    pivot = partition(lst, small, big, pivot)    
    
    if k == pivot:
        return lst[k:]
    if k < pivot:
        return quick_select(lst,

def partition(lst, small, big, pivot)

def test():
    assert k_closest([], 0) == []
    assert k_closest(zip(range(1,5), range(1,5)), 2) == [(2,2), (1,1)]

if __name__ == "__main__":
    test()

