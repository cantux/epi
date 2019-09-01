
#!/usr/bin/env python

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def create_ll_from_lst(lst):
    l = Node(None)
    curr = l
    for i in lst:
        curr.next = Node(i)
        curr = curr.next
    return l.next

def print_ll(l):
    curr = l
    while curr != None:
        print curr.value
        curr = curr.next

def add_nums(r, l):
    carry = 0
    ret = Node(None)
    ret_head = ret
    while r or l or carry:
        val = (r.value if r else 0) + (l.value if l else 0) + carry
        ret.next = Node(val % 10)
        carry = val // 10
        r, l, ret = r.next if r else None, l.next if l else None, ret.next

    return ret_head.next

def test():
    l = create_ll_from_lst([3, 7, 7])
    r = create_ll_from_lst([7, 3, 3])
    print_ll(add_nums(l, r))

    l = create_ll_from_lst([3, 3])
    r = create_ll_from_lst([3, 7, 7])
    print_ll(add_nums(l, r))
    assert 1 == 1

if __name__ == "__main__":
    test()

