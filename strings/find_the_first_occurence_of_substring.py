# decomp
# interface
# brute force
# test cases
# optimization
# test cases
# dry run
# debugging

# given text of length n and pat length m,
# brute force algo is to try walking both inputs O(nm)
def find_first_substr_rolling_hash(text, pat):
    if not pat or not text or len(pat) > len(text):
        return -1
    
    pat_len = len(pat)
    pat_hash = hash(pat)
    for i, ch in enumerate(text):
        if pat_len + i <= len(text):
            if pat_hash == hash(text[i: pat_len + i]):
                return i
        else:
            return -1

# think of a small alphabet initially, decimal alphabet
def find_first_substr_rh(text, pat):
    if not pat or not text or len(pat) > len(text):
        return -1
 
    A_S = 256
    # calculate initial hash
    pat_hash = 0
    text_hash = 0
    for i in range(len(pat)):
        pat_hash += (A_S ^ (i + 1)) * ord(pat[i])
        text_hash += (A_S ^ (i + 1)) * ord(text[i])
    
    if text_hash == pat_hash: return 0

    for i in range(len(text) - len(pat)):
        text_hash += A_S ^ len(pat) * ord(text[i])
        text_hash *= A_S
        text_hash -= A_S * ord(text[i + len(pat)])
        if text_hash == pat_hash: 
            return len(pat) + i

    return -1


def test():
    assert find_first_substr_rh("", "") == -1
    assert find_first_substr_rh("a", "") == -1
    assert find_first_substr_rh("", "b") == -1
    assert find_first_substr_rh("b", "b") == 0
    assert find_first_substr_rh("b", "bb") == -1
    assert find_first_substr_rh("ab", "b") == 1
    assert find_first_substr_rh("aba", "ba") == 1
    assert find_first_substr_rh("aba", "aba") == 0
    assert find_first_substr_rh("ba", "ba") == 0
    assert find_first_substr_rh("zaba", "ba") == 2
    assert find_first_substr_rh("abaz", "ba") == 1
    assert find_first_substr_rh("abba", "ba") == 2


    assert find_first_substr_rolling_hash("", "") == -1
    assert find_first_substr_rolling_hash("a", "") == -1
    assert find_first_substr_rolling_hash("", "b") == -1
    assert find_first_substr_rolling_hash("b", "b") == 0
    assert find_first_substr_rolling_hash("b", "bb") == -1
    assert find_first_substr_rolling_hash("ab", "b") == 1
    assert find_first_substr_rolling_hash("aba", "ba") == 1
    assert find_first_substr_rolling_hash("aba", "aba") == 0
    assert find_first_substr_rolling_hash("ba", "ba") == 0
    assert find_first_substr_rolling_hash("zaba", "ba") == 2
    assert find_first_substr_rolling_hash("abaz", "ba") == 1
    assert find_first_substr_rolling_hash("abba", "ba") == 2

    find_first_substr_rh("aaa", "aa")


if __name__ == "__main__": 
    test()
