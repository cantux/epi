def is_p(a):
    l = len(a)
    k = 0
    while k < l // 2:
        if a[k] != a[-k - 1]:
            return False
        k += 1
    return True

def test():
    assert is_p("cannac")
    assert is_p("cananac")
    assert not is_p("rayaray") 

if __name__ == "__main__":
    test()
