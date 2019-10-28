#!/usr/bin/env python

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __eq__(self, other):
        return self.first == other.first

    def __lt__(self, other):
        return (self.first < other.first 
                if self.first != other.first
                else self.last < other.last)

    def __repr__(self):
        return self.first + " " + self.last

def test():
    lst = [Person("c", "c"), Person("c", "a"), Person("b", "b"), Person("b", "c")]
    lst.sort()
    print lst
if __name__ == "__main__":
    test()

