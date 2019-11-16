#!/usr/bin/env python
def fnc():
    return None

def test():
    dag = [("x", "s", 5), 
            ("x", "a", 3),
            ("s", "a", 2), 
            ("s", "b", 6), 
            ("a", "b", 7), 
            ("a", "c", 4), 
            ("a", "d", 2), 
            ("b", "d", 1),
            ("b", "c", -1),
            ("c", "d", -2),
            ]
 
    g = {}
    for d in dag:
        if d[0] not in g:
            g[d[0]] = []
        g[d[0]].append((d[1], d[2]))

    print g
    assert fnc() == None

if __name__ == "__main__":
    test()

