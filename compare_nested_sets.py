# equivalent or equal - strings or other sets 
# setEquals(s1, s2) -> True/False


"""
s1 -> "A"
s2 -> "A" ("A") -flatten-> s2 -> "A"

s1 -> "A" ("A" "B")
s2 -> "A" ("B" "A")

s1 -> "A" ( ("A" "B") "B") ("B")
s2 -> "A" ("B" "A") 

"A" =/= ("A") 

("a", "b") == ("b", "a") 

s1 -> "a" -> ("a", 0)
s2 -> 
ty

"""

import functools 

# 0 = equal, -1 if obj1 < obj2 , 1 if obj1 > obj2
# sorted(lst, key=functools.cmp_to_key(comparator))
# [ ["a"] ["a", "b"] "t" "q" ] 
# [ "q" "t" ["a"] ["b"] ["a" "b"]]

def rec_compare(a, b):
    if type(a) == list and type(b) == list:
        if len(a) != len(b):
            return 1 if len(a) > len(b) else -1
        else:   
            for a_el, b_el in zip(
                    sorted(a, key=functools.cmp_to_key(rec_compare)), 
                    sorted(b, key=functools.cmp_to_key(rec_compare))):
                tmp = rec_compare(a_el, b_el) 
                if tmp != 0:
                    return tmp
            return 0
    elif type(a) == list:
        return 1
    elif type(b) == list:
        return -1
    elif a == b:
        return 0
    elif a < b:
        return -1
    return 1
    
def setEquals(s1, s2):
    # see if lengths are same
    def rec_sort(curr):
        res = []
        if type(curr) == list:
            for el in curr:
                res.append(rec_sort(el))
        else:
            res.append(curr)
        return sorted(res, key=functools.cmp_to_key(rec_compare))
    
    list_s1 = rec_sort(s1)
    # print(list_s1)
    list_s2 = rec_sort(s2)
    # print(list_s2)
    
    print(sorted(s1, key=functools.cmp_to_key(rec_compare)))
    print(sorted(s2, key=functools.cmp_to_key(rec_compare)))

    def rec_equal(l1, l2):
        if type(l1) == list and type(l2) == list:
            if len(l1) != len(l2):
                return False
            for el1, el2 in zip(l1, l2):
                if not rec_equal(el1, el2):
                    return False
            return True
        if type(l1) == list or type(l2) == list:
            return False
        elif l1 == l2:
            return True
        return False
    
    return rec_equal(list_s1, list_s2)
    
print(setEquals(["a"], ["a"]))
print(setEquals([], []))
print(setEquals(["a", "b"], ["a", "b"]))
print(setEquals(["b", "a"], ["a", "b"]))

print(setEquals(["a", "b", "c"], ["a", "b", ["c"]]))
print(setEquals(["a", "b", ["c"]], ["a", "b", ["c"]]))

