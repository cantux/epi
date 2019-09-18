class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class QueueEmptyException(Exception):
    pass

class Queue(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enque(self, value):
        node = Node(value)
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def deque(self):
        if self.tail.prev != self.head:
            rem = self.tail.prev
            rem.prev.next = self.tail
            self.tail.prev = rem.prev
            return rem.value
        raise QueueEmptyException()

    def toList(self):
        lst = []
        if self.head.next != self.tail:
            curr = self.head.next
            while curr != self.tail:
                lst.append(curr.value)
                curr = curr.next
        return lst

    def print_q(self):
        if self.head.next != self.tail:
            curr = self.head.next
            while curr != self.tail:
                print curr.value
                curr = curr.next

def test():
    q = Queue()
    q.enque(1)
    q.enque(2)
    assert q.toList() == [2, 1]
    assert q.deque() == 1
    assert q.toList() == [2]
    q.enque(3)
    q.enque(4)
    assert q.toList() == [4, 3, 2]
    assert q.deque() == 2
    assert q.deque() == 3
    assert q.toList() == [4] 

if __name__ == "__main__":
    test()
        
