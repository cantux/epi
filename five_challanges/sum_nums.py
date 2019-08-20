def sums_for(l):
    res = 0
    for i in l:
        res += i
    return res

def sums_while(l):
    i, res = 0, 0
    while i < len(l):
        res += l[i]
        i += 1
    return res

def sums_r(l):
    res = 0
    if not l:
        return res
    return res + sums_h(l, 0)

def sums_h(l, c):
    if c == (len(l) - 1):
        return l[c]
    return l[c] + sums_h(l, c + 1)

def test():
    inpu = [
            [0, 1, 2, 3],
            [5, 10],
            [],
            [0],
            [5, 5],
            [1],
    ]
    o = [
            6,
            15,
            0,
            0,
            10,
            1
    ]
    
    for i, inp in enumerate(inpu):
         assert sums_for(inp) == sums_while(inp) == sums_r(inp) == o[i]
    

if __name__ == "__main__":
    test()
