"""
    A -> 0
    B -> 1
    .
    .
    AA -> 27
    AB -> 28
    .
    .
    BA -> 53
    BB -> 54
    .
    .
    ZA -> 26*26 + 1
    create encoder and decoder.
"""

import math

char_mp = {chr(x + 97): x for x in range(26) }
num_mp = {num: ch for ch, num in char_mp.items()}

def enc(text):
    txt_len = len(text)
    pos = 0
    for i, ch in enumerate(text):
        pos += char_mp[ch] + 26 * (txt_len - i - 1)
    return pos

def dec(pos):
    res = pos // 26
    rem = pos % 26
    if res == 0:
        return num_mp[rem]
    return num_mp[rem] + dec(res - 1)

def test():
    assert dec(enc('e')) == 'e'
    assert enc(dec(26)) == 26

if __name__ == "__main__":
    test()
