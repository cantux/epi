#!/usr/bin/env python

class List:
    def __init__(self, val):
        self.val = val
        self.next = None


def fnc(L1, L2):
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
    L = List(3)
    L.next = List(5)
    L.next.next = List(6)

    L2 = List(4)
    L2.next = List(7)
    L2.next.next = List(8)
    
    a = fnc(L, L2)
    while a:
        print a.val
        a = a.next

if __name__ == "__main__":
    test()

