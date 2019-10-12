#!/usr/bin/env python

from collections import Counter

def fnc(sentence, words):
    not_enc = Counter(words)
    len_s = len(sentence)
    len_w = len(words[0])
    missing = len_w
    window_size = len_w * len(words)
    if window_size > len_s or len_s == 0 or len_w == 0: return ""
    left, right = 0, 0
    print "first: ", not_enc
    temp = ""
    while right < window_size:
        temp += sentence[right]
        right += 1
        if right % len_w == 0:
            if temp in not_enc:
                missing -= not_enc[temp] > 0
                not_enc[temp] -= 1
            temp = ""
    print "after init: ", not_enc
    print "after init missing: ", missing
    if missing == 0: return sentence[:right]

    while right < len_s:
        # look at the last first word, if it was in the counter remove it
        last_word = sentence[left:left + len_w]
        if last_word in not_enc:
            missing += not_enc[last_word] >= 0
            not_enc[last_word] += 1
        
        print "after window: ", not_enc
        print "after window missing: ", missing
        left += 1
        temp = ""
        for i in range(window_size):
            temp += sentence[left + i]
            if i % len_w == 0:
                if temp in not_enc:
                    missing -= not_enc[temp] > 0
                    not_enc[temp] -= 1
            temp = ""
        
        if missing == 0: 
            print left
            print right 
            return sentence[left - 1: right] 
        right += 1

    return ""

def test():
#     words = ["ab", "bc"]
#     sentence = "abbc"
#     assert fnc(sentence, words) == "abbc"

    words = ["ab", "bc"]
    sentence = "aabbc"
    assert fnc(sentence, words) == "abbc"
    words = ["ab", "bc"]
    sentence = "abbca"
    assert fnc(sentence, words) == "abbc"
    words = ["ab", "bc"]
    sentence = "asdfabbc"
    assert fnc(sentence, words) == "abbc"
    words = ["ab", "bc"]
    sentence = "ababbc"
    assert fnc(sentence, words) == "abbc"
    words = ["ab", "bc"]
    sentence = "abrgbc"
    assert fnc(sentence, words) == ""




if __name__ == "__main__":
    test()

