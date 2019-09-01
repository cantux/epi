from linked_list import Node

def rem_node(head, node):
    prev = None
    curr = head

    while curr != None:
        if curr == node:
            if prev != None:
                prev.next = curr.next
            else:
                head = head.next
        prev = curr
        curr = curr.next

def test():
    lst = [Node(i) for i in range(5)]
    create_list(lst)
    print_lst(lst[0])
    
    rem_node(lst[0], lst[1])
    print "after rem"
    print_lst(lst[0])

def create_list(lst):
    for i in range(len(lst) - 1):
        lst[i].next = lst[i + 1] 

def  print_lst(head):
    curr = head
    while curr != None:
        print "val is: ", curr.value
        curr = curr.next


if __name__ == "__main__":
    test()
