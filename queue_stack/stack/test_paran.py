paran_dct = {']': '[', ')': '(', '}': '{'}
def test_paran(text):
    tokens = text.split(',')
    paran_stack = []
    for t in tokens:
        if t in paran_dct:
            if paran_stack: 
                curr = paran_stack.pop()
            else: 
                return False
            if curr != paran_dct[t]:
                return False
        else:
            paran_stack.append(t)
    return not paran_stack


def test():
    assert test_paran("(,)")
    assert test_paran("[,(,),]")
    assert not test_paran("[,(,),],[")
    assert not test_paran("[,(,),],]")
    assert 1 == 1

if __name__ == "__main__":
    test()

