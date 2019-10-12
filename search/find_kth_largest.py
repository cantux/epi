
#!/usr/bin/env python
import heapq
import random
def kth(lst, k):
    if not lst: return None
    if len(lst) <= k: return None
    h = []
    h.append(lst[0])
    for i in range(1, len(lst)):
        curr = lst[i]
        if len(h) == k:
            if curr >= h[0]:
                heapq.heappop(h)
                heapq.heappush(h, curr)
        else:
            heapq.heappush(h, curr)
    return h[0]
   
def part_kth(lst, k):
    # make use of quicksort's partition algorithm
    # so I will choose a random element and pivot around it
    # then check if the position is on the left or the right of our given pivot position and choose a half
    lst_len = len(lst)
    piv_start = 0
    piv_end = lst_len - 1
    while piv_start < piv_end:
        random_piv_idx = random.randint(piv_start, piv_end)
        found_idx = part_around_el(lst, random_piv_idx, piv_start, piv_end)
        if found_idx == lst_len - k:  # ([0 1 2 3 4], k) -> (x, 2) -> 3, (x, 3) -> 2 -> len - k
            return lst[lst_len - k]
        elif lst_len - k > found_idx: # k is larger than el_idx
            piv_start = found_idx + 1
        else:
            piv_end = found_idx - 1

    return lst[piv_start]

def part_around_el(lst, piv_idx, piv_start, piv_end):
    if piv_start >= piv_end:
        return piv_idx

    pivot = lst[piv_idx]
    lst[piv_idx], lst[piv_end] = lst[piv_end], lst[piv_idx]

    small_ptr = piv_start
    big_ptr = piv_end - 1 
    last_big = False
    while small_ptr < big_ptr:
        if lst[small_ptr] > pivot:
            lst[small_ptr], lst[big_ptr] = lst[big_ptr], lst[small_ptr]
            big_ptr -= 1
        else:
            small_ptr += 1

    if lst[small_ptr] <  pivot:
        small_ptr += 1
            
    lst[piv_end], lst[small_ptr] = lst[small_ptr], lst[piv_end]
    return small_ptr


def shuffle(lst):
    i = 0
    for i in range(len(lst)):
        pos = random.randint(i, len(lst) - 1)
        lst[i], lst[pos] = lst[pos], lst[i]
 
def test():
    lst = range(10)
    shuffle(lst)
    assert part_kth(lst, 4) == 6
    assert kth(lst, 4) == 6
    assert part_kth(lst, 3) == 7
    assert kth(lst, 3) == 7
    assert part_kth(lst, 2) == 8
    assert kth(lst, 2) == 8
    assert part_kth(lst, 1) == 9
    assert kth(lst, 1) == 9
    assert part_kth(lst, 9) == 1
    assert kth(lst, 9) == 1

    lst = range(100)
    for _ in range(100):
        shuffle(lst)
        for i in range(1, len(lst)):
            assert part_kth(lst, i) == len(lst) - i
            assert kth(lst, i) == len(lst) - i

if __name__ == "__main__":
    test()

