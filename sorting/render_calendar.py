#!/usr/bin/env python

def fnc(calendar):
    lst = []
    for i, (start, fin) in enumerate(calendar):
        lst.append((start, "s"))
        lst.append((fin, "f"))

    
    lst.sort(key=lambda x: x[0])
    print "sorted list is: ", lst
    
    found_start, found_end = 0, lst[-1][0]
    max_count, curr_count = 0, 0
    for el in lst:
        if el[1] == "s":
            curr_count += 1
            if max_count < curr_count:
                max_count = curr_count
                found_start = el[0]
        else:
            if curr_count == max_count:
                found_end == el[0]
            curr_count -= 1

    print found_start, found_end
    print max_count
    return None

def test():
    calendar = [
            (7, 10),
            (0, 5),
            (2, 4),
            (7, 10),
            (3, 6),
            (7, 10),
            (7, 10)]
    assert fnc(calendar) == None


if __name__ == "__main__":
    test()

