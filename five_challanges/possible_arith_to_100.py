# 12 + 3 - 4 + 56 - 6 + 7 + 89 = 100

# f(1..9) = 100

# f(2..9) = 99 or f(2..9) = 101

# f(3..9) = f(2..9) + 2

# f(3..9) = f(2..9) - 2

# f(3..9) = f(1..9) - 12
# f(3..9) = f(1..9) + 12

# f(1..2) = 1 + 2
# f(1..2) = 

def find():
    l = []
    for c in combinations:
        if c[0] == True:
            l.append(c)
    return l
    

def test():
    assert 1 == 1

if __name__ == "__main__":
    test()
