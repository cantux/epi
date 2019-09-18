import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class EmptyStackException(Exception):
    pass

class MaxStack():
    def __init__(self):
        self.top = None
        self.max = -sys.maxint - 1

    def push(self, value):
        if value >= self.max:
            ins = Node(value)
            mx = Node(self.max)
            ins.next = mx
            mx.next = self.top
            self.max = value
            self.top = ins 
        else:
            ins = Node(value)
            ins.next = self.top
            self.top = ins

    def pop(self):
        val = 0
        if self.top:
            if self.peek() == self.max:
                val = self.top.value
                self.max = self.top.next.value
                self.top = self.top.next.next
            else:
                val = self.top.value
                self.top = self.top.next
            return val
        raise EmptyStackException()
    
    def peek(self):
        if self.top:
            return self.top.value
        raise EmptyStackException()

    def get_max(self):
        return self.max

def test():
    s = MaxStack()
    try:
        s.peek()
        assert False
    except(EmptyStackException):
        assert True

    s.push(1)
    assert s.peek() == 1
    assert s.pop() == 1
    try:
        s.peek()
        assert False
    except:
        assert True
    s.push(1)
    assert s.get_max() == 1
    s.push(2)
    assert s.get_max() == 2
    s.pop()
    assert s.get_max() == 1

    s.push(3)
    s.push(4)
    assert s.get_max() == 4
    s.pop()
    s.pop()
    assert s.get_max() == 1

if __name__ == "__main__":
  test()

