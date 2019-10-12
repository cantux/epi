#!/usr/bin/env python

from collections import Counter

def anon_letter(mag, letter):
    letter_freq_map = Counter(letter)
    for ch in mag:
        if ch in letter_freq_map:
            letter_freq_map[ch] -= 1
            if letter_freq_map[ch] == 0:
                del letter_freq_map[ch]
    return not letter_freq_map

def test():
    assert anon_letter("", "")
    assert anon_letter("asdf", "as")
    assert anon_letter("ffds", "fdsf")
    assert not anon_letter("ffds", "fdsfa")
    assert anon_letter("aaaa", "a")
    assert not anon_letter("aaaa", "aaaaa")

if __name__ == "__main__":
    test()

