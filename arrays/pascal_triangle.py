####
##  USE ITERATION instead of recursion.
##
####
def create_pascal_row(level):
    if level == 0:
        return [1]
    return add_arrs(create_pascal_row(level - 1))

def c_p_r(level):
    mem = [[1], [1, 1]]
    c_p_rr(level, mem)
    return mem

def c_p_rr(level, mem):
    if level < len(mem):
        return mem[level]
    mem.append(c_p_rr(level - 1, mem))
    return mem[level]

def add_arrs(a):
    r = []
    r.append(a[0])
    i = 1
    while i < len(a):
        r.append(a[i - 1] + a[i])
        i += 1
    r.append(a[len(a) - 1])
    return r
    
def test():
#     assert create_row([1]) == [1, 1]
#     assert create_row([1, 1]) == [1, 2, 1]
    print(create_pascal_row(0))
    print(create_pascal_row(1))
    print(create_pascal_row(2))
    
    print(c_p_r(0))
    print(c_p_r(1))
    print(c_p_r(2))

if __name__ == "__main__":
    test()
