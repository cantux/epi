#!/usr/bin/env python

def fnc(text):
    # go over the whole text
    # for every point expand out until we hit the previous palindrome or the string beginning.
    # set the beginning to be the end of last palindrome.
    # don't forget that a palindrome contains a palindrom and single char palindromes around it.
    
    ret = [] # a list of lists [[], []]
    len_txt = len(text)
    def helper(begin, curr_lst):
        if begin >= len_txt:
            ret.append(list(curr_lst))
        for i in range(begin, len_txt):
            if text[begin] == text[i]:
                if dp_pal_check(begin, i):
                    curr_lst.append(text[begin:i + 1])
                    helper(i + 1, curr_lst)
                    curr_lst.pop()

    dp = {}
    def dp_pal_check(begin, end):
        if (begin, end) in dp:
            return dp[(begin, end)]
        if begin + 1 == end:
            result = text[begin] == text[end]
            dp[(begin, end)] = result
            return result
        elif begin == end:
            return True
        else:
            if text[begin] == text[end]:
                result = dp_pal_check(begin + 1, end - 1)
                dp[(begin, end)] = result
                return result
            else:
                return False

    def palindrome_check(begin, end):
        if begin + 1 == end or begin == end:
            return text[begin] == text[end]
        if text[begin] == text[end]:
            return palindrome_check(begin + 1, end - 1)
        return False
        
    helper(0, [])
    return ret

def test():
    
    res1 = fnc("aab") 
    exp1 = [["aa", "b"], ["a", "a", "b"]]
    assert all([r in exp1 for r in res1])

    res2 = fnc("aabb")
    exp2 = [["a", "a", "b", "b"], ["aa", "bb"], ["aa", "b", "b"], ["a", "a", "bb"]]
    assert all([r in exp2 for r in res2])

if __name__ == "__main__":
    test()

