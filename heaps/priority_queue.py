
#!/usr/bin/env python

import heapq
import itertools

class MyHeapItem:
    counter = itertools.count()
    def __init__(self, value=None):
        self.tombstone = False
        self.value = value
        self.count = next(MyHeapItem.counter)

    def __str__(self):
        return str(self.value) + " " \
                + str(self.count) + " " \
                + f"is_tombstone: {self.tombstone}"

class MyHeap:
    def __init__(self):
        self.h = []
        self.entry_finder = {}

    def push(self, item, priority):
        if item.count in entry_finder:
            # remove the current item
            # update it's priority and reinsert it

        entry = [priority, item.count, item.value]

    def remove_task(self, item):
        item = self.entry_finder.pop(item.count)
        item.tombstone = True
    def pop():

def fnc():
    return None

def test():
    h_i_1 = MyHeapItem(1)
    h_i_2 = MyHeapItem(2)

    print(h_i_1)
    print(h_i_2)
    assert fnc() == None

if __name__ == "__main__":
    test()

