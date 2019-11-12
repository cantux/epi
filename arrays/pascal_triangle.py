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
    
def pt_dp(row):
    a = [1] * (row)
    i = 0
    while i < row:
        j = 1
        while j <= i // 2:
            a[j] = a[j] + a[j - 1]
            j += 1
        k = j
        while j < i:
            a[j] = a[k]
            j += 1
            k -= 1
        i += 1
    print a
    return a

def pascaline(n):
    n = n - 1
    line = [1]

    for k in range(max(n ,0)):

        line.append(int(line[k]*(n-k)/(k+1)))

    return line

def test():
#     assert create_row([1]) == [1, 1]
#     assert create_row([1, 1]) == [1, 2, 1]
#     print(create_pascal_row(0))
#     print(create_pascal_row(1))
#     print(create_pascal_row(2))
    
#     print(c_p_r(0))
#     print(c_p_r(1))
#     print(c_p_r(2))
    pt_dp(3)
    pt_dp(2)
    pt_dp(1)
    pt_dp(4)
    pt_dp(5)

if __name__ == "__main__":
    test()
