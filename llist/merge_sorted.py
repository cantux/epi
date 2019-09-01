from linked_list import LinkedList, Node 

def merge_sorted(l1, l2):
    curr1 = l1
    curr2 = l2
    tail = ret = Node(None)

    while curr1 and curr2:
        if curr1.value <= curr2.value:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next

    if curr1 == None:
        tail.next = curr2
    else:
        tail.next = curr1
    return ret.next

def test():
    l1 = LinkedList([1, 3, 5])
    l2 = LinkedList([2, 4])
    ret_l = merge_sorted(l1.head.next, l2.head.next)
    l3 = LinkedList(ret_l)
    assert l3.toList() == [1, 2, 3, 4, 5] 

if __name__ == "__main__":
    test()
