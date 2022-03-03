
#!/usr/bin/env python

# https://leetcode.com/problems/last-stone-weight-ii/
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. 
# Suppose the stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

# PONDER
# smallest possible stone
# let's imagine an optimal solution
# at the i th smash, i am smashing stones with weights u and v
# this adds a (u - v) size stone back to my pile and I go on to make an optimal choice etc.
# 
# building from the smallest possible solution, 
# here are some heuristics:
# does destroying stones give me an optimal solution?

# how to describe an optimal solution
# best solution is to have 0
# if I could make sure the summation of a certain partition of the array is smallest
# is greedy choice the best? NOPE
# THIS IS KNAPSACK DP, we will get back to it.
def fnc():


    return None

def test():
    stones = [2, 7, 4, 1, 8, 1]
    assert fnc(stones) == 1
    assert fnc([31,26,33,21,40]) == 5
    assert fnc([1, 2]) == 1


if __name__ == "__main__":
    test()

