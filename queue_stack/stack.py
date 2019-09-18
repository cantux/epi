class Stack(object):
    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
    
    class StackEmptyException(Exception):
        pass

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise StackEmptyException()

    def push(self, value):
        new = Node(value)
        new.next = self.top
        self.top = new

    def peek(self):
        if self.top:
            return self.top.value
        raise StackEmptyException()
