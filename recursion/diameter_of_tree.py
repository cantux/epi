
#!/usr/bin/env python

import sys
import heapq

class NaryTree():
    def __init__(self):
        self.children = []

    def add_child(self, child, edge_val):
        self.children.append((child, edge_val))


max_length = -sys.maxint - 1

def fnc(t):    
# find the max of the siblings
# max length can be the sum of them or we return the max length child to parents
    def find_rec(curr):
        if not curr.children:
            return 0

        children_lengths = []
        for ch, edge_val in curr.children:
            heapq.heappush(children_lengths, (edge_val + find_rec(ch)) * -1)

        max_child = heapq.heappop(children_lengths) * -1
        second_max = children_lengths[0] * -1 if children_lengths else 0

        global max_length
        max_length = max(second_max + max_child, max_length)

        return max_child

    find_rec(t)
    return max_length

def test():
    nodes_list = []
    for _ in range(7):
        nodes_list.append(NaryTree())

    nodes_list[0].add_child(nodes_list[1], 50)
    nodes_list[0].add_child(nodes_list[2], 49)
    nodes_list[1].add_child(nodes_list[3], 100)
    nodes_list[1].add_child(nodes_list[4], 1)
    nodes_list[4].add_child(nodes_list[5], 100)
    nodes_list[4].add_child(nodes_list[6], 100)

    assert fnc(nodes_list[0]) == 201

if __name__ == "__main__":
    test()

