
#!/usr/bin/env python

# https://leetcode.com/problems/single-row-keyboard/
# There is a special keyboard with all keys in a single row.

# Given a string keyboard of length 26 indicating the layout of the keyboard 
# (indexed from 0 to 25). Initially, your finger is at index 0. 
# To type a character, you have to move your finger to the index of the desired 
# character. The time taken to move your finger from index i to index j is |i - j|.

# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.


def fnc(s, w):
    mp = {c: i for i, c in s}
    tot = 0
    for c1, c2 in zip(w, w[1:]):
        tot += abs(mp[c2] - mp[c1])
    return tot + mp[w[0]]

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

