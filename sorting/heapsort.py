
#!/usr/bin/env python

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

