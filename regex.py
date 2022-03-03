#!/usr/bin/env python


def match_reg(ptrn, txt):
    for i in range(len(txt)):
        if match(ptrn, txt, 0, i):
            return True
    return False


def match(ptrn, txt, current_ptrn_idx, current_txt_idx):
    if current_ptrn_idx >= len(ptrn):
        return True

    if current_txt_idx >= len(txt):
        if len(ptrn) > current_ptrn_idx + 1:
            return ptrn[current_ptrn_idx + 1] == '*'
        else:
            return False

    current_ptrn_ch = ptrn[current_ptrn_idx]
    current_txt_ch = txt[current_txt_idx]

    is_match = current_ptrn_ch == current_txt_ch or current_ptrn_ch == '.'

    # ptrn_ch '*'
    if current_ptrn_idx + 1 < len(ptrn) and ptrn[current_ptrn_idx + 1] == '*':
        # previous ptrn_ch matches current
        if is_match:
            return match(ptrn, txt, current_ptrn_idx, current_txt_idx + 1)
        # ptrn_ch doesn't match current, could be the zero case for *
        else:
            return match(ptrn, txt, current_ptrn_idx + 2, current_txt_idx + 1)
    # ptrn_ch match or '.'
    elif is_match:
        return match(ptrn, txt, current_ptrn_idx + 1, current_txt_idx + 1)
    return False


# if sys.stdin:
#     for line in sys.stdin:
#         print match_reg(line, sys.argv[0])
# else:
#     print match_reg(sys.argv[0], sys.argv[1])


def test():
    assert match_reg("ab", "ab")
    assert match_reg("ab", "abx")
    assert match_reg("ab", "xab")
    assert match_reg("ab", "ab")
    assert match_reg("ab", "aab")
    assert not match_reg("abc", "aab")
    assert not match_reg("ab", "axb")

    assert match_reg("a.", "aa")
    assert not match_reg("a.", "a")
    assert not match_reg("a.", "ba")
    assert match_reg("a.c", "abc")
    assert match_reg(".c", "ac")

    # assert match_reg("a*", "")
    assert match_reg("a*", "abbbbc")
    assert match_reg("a*", "aaaaa")
    assert match_reg("a*", "b")

    assert match_reg("ab*", "abbbbc")
    assert match_reg("ab*", "abbbb")
    assert match_reg("ab*", "a")
    assert match_reg("ab*", "ab")
    assert match_reg("ab*", "bbbbba")
    assert match_reg("ab*", "ac")
    assert match_reg("ab*", "a")

    assert match_reg(".*", "a")
    assert match_reg(".*", "ab")
    assert match_reg("a.*b", "ab")
    assert match_reg("a.*b", "acb")

    # assert match_reg(".*", "")
    assert not match_reg("a.*b", "ac")



if __name__ == "__main__":
    test()