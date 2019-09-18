
#!/usr/bin/env python

from collections import deque

class Queue():
    def __init__(self):
        self.right = []
        self.left = deque([])

    def enqueue(self, val):
        self.left.append(val)

    def dequeue(self):
        if not self.right:
            while self.left:
                self.right.append(self.left.pop())
        return self.right.pop()

def test():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    q.enqueue(5)
    assert q.dequeue() == 4

if __name__ == "__main__":
  test()

