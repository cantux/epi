#!/usr/bin/env python

from collections import Counter
import heapq

class Stack:
    def __init__(self):
        self.c = 1 
        self.s = []

    def push(self, val):
        heapq.heappush(self.s, (self.c * -1, val))
        self.c += 1

    def peek(self):
        return self.s[0][1]

    def pop(self):
        return heapq.heappop(self.s)[1]

def test():
    s = Stack()
    s.push(0)
    assert s.peek() == 0
    s.push(1)
    assert s.peek() == 1
    assert s.pop() == 1
    assert s.peek() == 0

if __name__ == "__main__":
  test()

