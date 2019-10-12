#!/usr/bin/env python

def pal_per(s):
    char_set = set()

    for ch in s: 
        if ch in char_set:
            char_set.remove(ch)
        else:
            char_set.add(ch)

    return len(char_set) < 2

def test():
    assert pal_per("aa")
    assert pal_per("a")
    assert pal_per("")
    assert pal_per("aab")
    assert pal_per("aabb")
    assert pal_per("aabbc")
    assert not pal_per("aabbdc")
    assert not pal_per("abc")
    assert not pal_per("ab")

if __name__ == "__main__":
  test()

