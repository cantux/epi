#!/usr/bin/env python

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return "name: {0}, gpa: {1}".format(self.name, self.gpa)

def fnc():
    return None

def test():
    s_list = [Student(x, 10) for x in range(10)[::-1]]
    print(map(str, s_list))
    print(map(str, sorted(s_list)))

    print(map(str, s_list))
    s_list.sort(key=lambda student: student.name)
    print(map(str, s_list))

    str_sort = [0, 2, 110]
    print(sorted(str_sort, key= lambda x: str(x)))
    rev = range(10)[::-1]
    sorted_rev = list(rev).sort()
    print(sorted_rev)


    print("sort multiple keys: ")
    l = [(1, 0), (2, 1), (3,4), (3,3)]
    print("normal: " + str(sorted(l)))
    print("second item based: " + str(sorted(l, cmp=lambda x: (x[1], x[0]))))

    
    assert fnc() == None

if __name__ == "__main__":
    test()

