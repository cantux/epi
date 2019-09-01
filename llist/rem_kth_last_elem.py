from linked_list import Node

c = 0
def trav(curr, prev, k):
    if curr == None:
        return
    trav(curr.next, curr, k)
    global c
    c += 1
    if c == k:
        prev.next = curr.next

def rem_kth_last(l, k):
    trav(l, None, k)

def test():
    lst = [Node(i) for i in range(5)]
    for i in range(len(lst) - 1):
        lst[i].next = lst[i+1]
        
    rem_kth_last(lst[0], 2)
    print_lst(lst[0])

def print_lst(head):
    curr = head
    while curr != None:
        print curr.value
        curr = curr.next

if __name__ == "__main__":
    test()
