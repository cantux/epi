# 1 11 21 1211 111221 312211

# write a program that returns the nth look and say

# brute force algo
# run a pointer on each token encounter keep a count and reset the count either at the end or upon encountering a new token

# some decomposition on the problem
# we will be appending to a new array each time. so normally we would want to use a linked list here.
# can I assume this is some sort of a vector structure? vector resizes itself on some given load factor right?
# so we don't have to worry about resizing
# we know that once we encounter a new token there will be two

def nth(n):
    return nth_helper(n, 1, '1')

def nth_helper(n, count, text):
    if n == count:
        return text
    new_text = construct_new_text(text)
    return nth_helper(n, count + 1, new_text)

def construct_new_text(text):
    curr = text[0] # no need to check if the first element exists.
    count = 1       # start from 1 to account for the first element.
    new_text = ""
    for i in range(1, len(text)):
        if curr == text[i]:
            count += 1
        else:
            new_text += str(count) + curr
            curr = text[i]
            count = 1
    new_text += str(count) + curr
    return new_text

def test():
    assert nth(1) == '1'
    assert nth(2) == '11'
    assert nth(3) == '21'
    assert nth(4) == '1211'
    assert nth(5) == '111221'
    assert nth(6) == '312211'

if __name__ == "__main__":
    test()
