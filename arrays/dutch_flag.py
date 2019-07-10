def p(piv_i, a):
    piv = a[piv_i]
    a[piv_i], a[-1] = a[-1], a[piv_i]
    big = len(a) - 1
    sm = 0
    i = 0
    while sm <= big:
        if a[i] <= piv:
            sm += 1
            i += 1
        else:
            a[i], a[big] = a[big], a[i]
            big -= 1



