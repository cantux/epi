#!/usr/bin/env python

def fnc(words, cols):
    if not words: return []
    w_l = []
    for i in xrange(len(words)):
        w_l.append = len(words[i])
    print words_sum

    while i < len(words):
        curr_count = 0
        curr_word_count = 0
        each_space = 0
        extra_space = 0
        while i < len(words):
            curr_count += w_l[i] + 1
            if curr_count - 1 > col:
                i -= 1
                curr_count -= w_l[i] - 1
                curr_word_count -= 1
                spaces = col - curr_count
                each_space = spaces // curr_word_count
                extra_space = spaces % curr_word_count
                break
                

            i += 1 
            curr_word_count += 1
        j = i
        while j < i + curr_word_count: 

            while each_space >= 0:
                if extra_space >= 0:

    return []
    

def test():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    assert fnc(words, maxWidth) == [
                                "This    is    an",
                                "example  of text",
                                "justification.  "
                                ]

if __name__ == "__main__":
    test()

