#!/usr/bin/env python
def fnc():
    return None

def test():
    # (source, dest, weight)
    vew = [("s", "a", 1), 
            ("s", "b", 2), 
            ("a", "c", 5), 
            ("a", "b", 3), 
            ("b", "a", 1), 
            ("a", "e", 2), 
            ("c", "e", 3),
            ("e", "f", 4),
            ("e", "d", 1),
            ("d", "c", 2),
            ("b", "d", 1),
            ("d", "f", 1),
            ]
    g = {}
    for d in vew:
        if d[0] not in g:
            g[d[0]] = []
        g[d[0]].append((d[1], d[2]))

    print g
    assert fnc() == None

if __name__ == "__main__":
    test()

