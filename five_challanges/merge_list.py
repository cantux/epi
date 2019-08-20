def merge_lists(a, b):
    l = []
    for i, a_el in enumerate(a):
        l.append(a_el)
        l.append(b[i])
    return l

def test():
    assert merge_lists([], []) == []
    assert merge_lists(['a'], [1]) == ['a', 1]

if __name__ == "__main__":
    test()
