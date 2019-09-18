
def norm(text):
    paths = text.split('/')
    p_stack = []
    if not paths[0]:
        p_stack.append('')
    for p in paths:
        if p and p != '.':
            if p == ".." and p_stack:
                p_stack.pop()
            else:
                p_stack.append(p)

    s = '/'.join(p_stack)
    print s
    return s

def test():
    assert norm("/a/b/c") == "/a/b/c"
    assert norm("") == ""
    assert norm("/") == ""
    assert norm("a/../b") == "b"
    assert norm("a/././b") == "a/b"
    assert norm("a/./../b") == "b"

if __name__ == "__main__":
    test()
