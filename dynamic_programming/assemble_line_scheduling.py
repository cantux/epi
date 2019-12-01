#!/usr/bin/env python

def fnc(a, t, e, x):
    len_assembly = len(a[0])
    
    dp_0 = [0] * len_assembly 
    dp_1 = [0] * len_assembly

    dp_0[0] = e[0] + a[0][0]
    dp_1[0] = e[1] + a[1][0]

    for time_spent_on_st_i_ptr in xrange(1, len_assembly):
        i = time_spent_on_st_i_ptr
        dp_0[i] = min(dp_0[i - 1] + a[0][i], dp_1[i - 1] + a[0][i] + t[1][i])
        dp_1[i] = min(dp_1[i - 1] + a[1][i], dp_0[i - 1] + a[1][i] + t[0][i])
    
    return min(dp_0[len_assembly - 1] + x[0], dp_1[len_assembly - 1] + x[1])


def carAssembly (a, t, e, x): 
      
    NUM_STATION = len(a[0]) 
    T1 = [0 for i in range(NUM_STATION)] 
    T2 = [0 for i in range(NUM_STATION)] 
      
    T1[0] = e[0] + a[0][0] # time taken to leave 
                           # first station in line 1 
    T2[0] = e[1] + a[1][0] # time taken to leave 
                           # first station in line 2 
  
    # Fill tables T1[] and T2[] using 
    # above given recursive relations 
    for i in range(1, NUM_STATION): 
        T1[i] = min(T1[i-1] + a[0][i], 
                    T2[i-1] + t[1][i] + a[0][i]) 
        T2[i] = min(T2[i-1] + a[1][i], 
                    T1[i-1] + t[0][i] + a[1][i] ) 
  
    # consider exit times and return minimum 
    return min(T1[NUM_STATION - 1] + x[0], 
               T2[NUM_STATION - 1] + x[1]) 

def test():
    aa = [
            [4, 5, 3, 2],
            [2, 10, 1, 4]
            ]
    ta = [
            [0, 7, 4, 5],
            [0, 9, 3, 8]
            ]

    ea = [
            10, 
            12
            ]
    xa = [18, 7]

    print carAssembly(aa, ta, ea, xa)
    assert fnc(aa, ta, ea, xa) == carAssembly(aa, ta, ea, xa)

    ab = [
            [7, 9, 3, 4, 8, 4],
            [8, 5, 6, 4, 5, 7]
            ]

    tb = [
            [0, 2, 3, 1, 3, 4],
            [0, 2, 1, 2, 2, 1]
            ]

    eb = [2, 4]
    xb = [3, 2]

    print carAssembly(ab, tb, eb, xb)
    assert fnc(ab, tb, eb, xb) == carAssembly(ab, tb, eb, xb)

if __name__ == "__main__":
    test()

