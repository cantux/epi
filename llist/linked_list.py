class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, lst=None):
        self.head = Node(None)
        if lst:
            if isinstance(lst, list):
                curr = self.head
                for i in lst:
                    curr.next = Node(i)
                    curr = curr.next
            elif isinstance(lst, Node):
                self.head.next = lst


    def toList(self):
        ret = []
        curr = self.head.next
        while curr != None:
            ret.append(curr.value)
            curr = curr.next
        return ret

