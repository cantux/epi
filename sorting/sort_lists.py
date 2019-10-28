#!/usr/bin/env python

class List:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        curr = self
        ret = ""
        while curr:
            ret += " " + str(curr.val)
            curr = curr.next
        return ret

def stable_sort_list(L):
    if not L or not L.next:
        return L
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None # splits the array
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))

def merge_two_sorted_lists(L1, L2):
    dummy_head = List(-1)

    prev = dummy_head
    while L1 and L2:
        if L1.val < L2.val:
            prev.next = L1
            L1 = L1.next
        else:
            prev.next = L2
            L2 = L2.next
        prev = prev.next

    prev.next = L1 or L2
    return dummy_head.next

def test():
    L = List(5)
    L.next = List(4)
    L.next.next = List(2)
    L.next.next.next = List(3)
    curr = stable_sort_list(L)
    while curr:
        print curr.val 
        curr = curr.next

if __name__ == "__main__":
    test()

