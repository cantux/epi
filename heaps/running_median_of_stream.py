#!/usr/bin/env python

# extra trick is to balance the sizes of the heaps.
import heapq
class LstMedian:
    def __init__(self):
        self.lst = []
        self.left = []
        self.right = []

    def get_med(self):
        len_lst = len(self.lst)
        if len_lst % 2 != 0:
            return self.left[0] * -1
        else:
            return ((self.left[0] * -1) + self.right[0]) * 0.5 

    def insert_data(self, data):
        self.lst.append(data)
        heapq.heappush(self.right, data)
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, heapq.heappop(self.right) * -1)


def test():
    lst_med = LstMedian()
    lst_med.insert_data(5)
    assert lst_med.get_med() == 5
    lst_med.insert_data(6)
    assert lst_med.get_med() == 5.5
    lst_med.insert_data(10)
    assert lst_med.get_med() == 6
    lst_med.insert_data(11)
    assert lst_med.get_med() == 8
if __name__ == "__main__":
  test()

