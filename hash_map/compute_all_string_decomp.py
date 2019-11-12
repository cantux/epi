#!/usr/bin/env python

from collections import Counter
import copy
# find the substring of the sentence which are the conataenation of all the words.
def fnc(sentence, words):
    len_w = len(words[0])
    d = {words}
    for i in range(len(sentence)):
        k = i
        temp = {}
        while k < len(sentence):
            curr_word = sentence[k:k + len_2]
            if curr_word in words:
                k = k + len_w + 1
                words.remove(curr_word)
                temp.add(curr_word)
            else:
                d = d.union(temp)
                break
            if not words:
                return sentence[i:k]
    return ""


def test():
    


if __name__ == "__main__":
    test()

