#!/usr/bin/env python

from rotate_list import Node, create_ll_from_lst, print_ll

def merge(l):
    # find the tail
    curr = l
    prev = None
    while curr != None:
        prev = curr
        curr = curr.next
    tail = prev

    curr = l
    toggle = 0
    while curr != tail:
        if toggle == 0:
            toggle = 1
            curr = curr.next
        else:
            nxt = curr.next
            tail.next = nxt
            tail = tail.next

            toggle = 0
            curr = curr.next
    
def merge_book(l):
    curr = l

    toggle = 0
    odd_start = odd_dummy_head = Node(None)
    even_dummy_head = even_start = Node(None)
    while curr != None:
        if toggle == 0:
            even_dummy_head.next = curr
            curr = curr.next
            even_dummy_head = even_dummy_head.next
            togge = 1
        else:
            odd_dummy_head.next = curr
            curr = curr.next
            odd_dummy_head = odd_dummy_head.next
            toggle = 0
    print "evens"
    print_ll(even_start.next)
    print "odds"
    print_ll(odd_start.next)

    even_dummy_head.next = odd_start.next
    l = even_start.next

def test():
    l = create_ll_from_lst(range(10))
    print_ll(l)
    merge_book(l)
    print_ll(l)
    assert 1 == 1

if __name__ == "__main__":
  test()

