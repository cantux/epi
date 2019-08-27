# given a word and a string s, find anagram occurrences in string.

# decomposition
# what is an anagram, does the frequencies matter? yes

# interface

# brute force solution
# n^2 go over the string and word ch by ch.

# test cases
# ab -> abcbab
# ab -> aabbacca
# ab -> ab
# '' -> ab -> I will handle this according to my convenience
# ab -> '' -> empty 

# dry run

# optimization
# create a frequency dictionary
# use sliding window to increase the removed char freq and decrease the newly added ch freq
# we can check if the freq list is empty is empty(therefore will be indicating an occurence
# [we can check if the freq map is empty in O(1) by keeping track of the number of encountered elements in the freq map and removing and adding to that number if the key exists. 
# When an element is removed we must check if its temporary frequency is already 0, if it is, we know for sure that it's not an anagram.)

# new test cases you can think of
# example to lose track: aabb -> aaabb

# dry run
# implementation
# debugging
# test cases
from collections import Counter, deque

def find_anagram_indeces(s, w):
    word_len = len(w)
    if len(s) < word_len:
        return []

    w_freq = Counter(w)
    leftover = word_len

    first = s[:word_len]
    window = deque(first)
    for ch in first:
        if ch in w_freq:
            w_freq[ch] -= 1
            leftover -= 1

    print("first: {0}".format(first))
    print("w_freq: {0}".format(w_freq))
    print("leftover: {0}".format(leftover))
    ret = []
    
    for i, ch in enumerate(s[word_len:]):
        rem = window.popleft()
        if rem in w_freq:
            w_freq[rem] += 1
            leftover += 1
        if ch in w_freq:
            w_freq[ch] -= 1
            leftover -= 1
            if w_freq[ch] == 0 and lefover == 0:
                ret.append(i)
        window.append(ch)

    return ret

def test():
    assert find_anagram_indeces("a", "a") == [0]
    assert find_anagram_indeces("ab", "a") == []
    assert find_anagram_indeces("a", "ab") == [0]
    assert find_anagram_indeces("a", "aa") == [0, 1]
    assert find_anagram_indeces("", "") == []

if __name__ == "__main__":
    test()
