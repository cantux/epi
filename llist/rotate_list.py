# decomp
# given a list, rotata the list by K
# if list is 0, 1, .. N
# after rotate it's gonna be K, K + 1, ... N, 0, 1, .. , K - 1

# all we have to do seems like 
# 1- remove the link from K -1 to K
# 2- append it to the tail

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

def rotate(l, k):
    curr = l
    prev = None
    count = 0
    k1th = None
    while curr != None:
        if k == count:
            k1th = prev
            k1th.next = None
        prev = curr
        curr = curr.next
        count += 1

    prev.next = l

def test():
    l = create_ll_from_lst(range(5))
    print_ll(l)
    rotate(l, 2) 
    print_ll(l)
#     assert == [3, 4, 0, 1, 2]


if __name__ == "__main__":
    test()

