

#!/usr/bin/env python

class DLLC:
    def __init__(self, val, nxt=None, prev=None, child=None):
        self.next = nxt
        self.prev = prev
        self.child = child 
        self.val = val

    def __repr__(self):
        return str(self.val)

def one_i_love(head):

    def rec(root):
        # base con

        # find the tail element
        tail = root
        while tail.next:
            tail = tail.next

        # for every node
        curr = root
        while curr:
            if curr.child:
                child_head, child_tail = rec(curr.child)
                # append child's accumulated head pointer to the tail element
                tail.next = child_head
                child_head.prev = tail
                # update the tail with child's tail
                tail = child_tail

                curr.child = None
            curr = curr.next

        # return head and tail
        return (root, tail)
    # what is the complexity of this approach? feel like O(n)    
    # It doesn't initially look like we can do better
    # we are looking for the tail element, that adds up to our complexity linearly too O(n + n)

    return rec(head)[0]

def fnc():
    return None

def test():
    lst = construct_list()
    assert one_i_love() == None

def construct_list():
    one = DLLC(1)

    return one
if __name__ == "__main__":
    test()

