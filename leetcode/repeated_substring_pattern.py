def old_repeatedSubstringPattern(self, s: str) -> bool:
    len_s = len(s)
    for i in range(1, (len_s // 2) + 1):
        if len_s % i == 0:
            h = hash(s[0:i])
            found = True
            for j in range(1, len_s // i):
                curr = s[j * i : (j + 1) * i]
                print(curr)
                curr = hash(curr)
                if h != curr:
                    found = False
                    break
            if found:
                return True
    return False

def repeatedSubstringPattern(s: str) -> bool:
    """
    Examples 
    abab -> ab will construct it
    aaaa -> a will construct it

    first idea, take the first letter repeat by the count, see if there is a match, n2
    divide into 2 then 3 then 4?
    """
    s_len = len(s)
    for curr_word_size in range(1, (s_len // 2) + 1):
        if curr_word_size % s_len == 0:
            possible_match = True
            word_count = s_len / curr_word_size
            for word_ptr in range(1, word_count + 1): 
                for char_ptr in range(curr_word_size):
                    if s[char_ptr] != s[(word_ptr * curr_word_size) + char_ptr]:
                        possbile_match = False
                        break
                if not possible_match:
                    break
            if possible_match:
                return True

    return False


if __name__ == "__main__":
    assert not repeatedSubstringPattern("a")
    assert not repeatedSubstringPattern("aba")
    assert repeatedSubstringPattern("aaa")
    assert repeatedSubstringPattern("abab")
    assert repeatedSubstringPattern("abcabcabc")
