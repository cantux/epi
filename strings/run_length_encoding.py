# decomp
# compress by zipping characters

# interface

# brute force
# on every encounter of a new character append to a new list the chars
# complexity is O(n), space O(n)

# test cases

# dry run

# optimization
# test cases
# dry run

def enc(text):
    if len(text) == 0:
        return ""
    # take the first char into a var named cmp(compared_var)
    # keep a count starting from 1
    comp = text[0]
    count = 1
    ret = ""

    # start the loop from the second char and compare it to the cmp
    # continue loop until we encounter a different char and increment count
    # if cmp and char is different insert count and the char, replace count and cmp
    for i in range(1, len(text)):
        if comp != text[i]:
            ret += comp + str(count)
            comp = text[i]
            count = 1
        else:
            count += 1

    ret += comp + str(count)
    return ''.join(ret)

def dec(cypher):
    # run 2 ptrs
    # append 2nd ptr * first ptr to new list.
    
    res = ""
    count = 0
    c_len = len(cypher)
    if c_len == 0:
        return res

    tmp = []
    for i in range(c_len):
        if cypher[i ].isdigit():
            count = count * 10 + int(cypher[i])
        else:
            tmp += int(cypher[i + 1]) * cypher[i]
    res = ''.join(tmp)
    return res
    
def test():
    assert enc("a") == "a1"
    assert enc("bb") == "b2"
    assert enc("abb") == "a1b2"
    assert enc("") == ""
    assert enc("cccbaa") == "c3b1a2"
    assert dec( enc("cccbaa") ) == "cccbaa"
    assert "a" == dec("a1")
    assert "bb" == dec("b2")
    assert "abb" == dec("a1b2")
    assert dec("") == ""
    assert "cccbaa" == dec("c3b1a2")


if __name__ == "__main__":
    test()
