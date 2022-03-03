
#!/usr/bin/env python

def totalFruit(fruit_types):
    """
    :type fruits: List[int]
    :rtype: int
    """
    # sliding window
    # find the max length subsequence that has only two types of fruit
    
    # O(n) and O(1) by keeping a start and an end ptr
    
    start, end = 0, 0
    
    len_f = len(fruit_types)
    
    current_type_mp = {}
    count = 0
    while end < len_f:
        curr = fruit_types[end]
        if curr in current_type_mp:
            current_type_mp[curr] = end
            end += 1
        elif fruit_types[end] not in current_type_mp and len(current_type_mp) == 2:
            min_idx = len_f + 1
            found_item = None
            found = False
            for typee, last_idx in current_type_mp.items():
                if last_idx < min_idx:
                    min_idx = last_idx
                    found_item = typee
                    found = True
            if found:
                start = current_type_mp[found_item] + 1
                del current_type_mp[found_item]
                current_type_mp[curr] = end
                end += 1
            else:
                assert False
        else:
            current_type_mp[curr] = end
            end += 1
        count = max(count, end - start)
        
    return count
               
def test():
    assert totalFruit([1, 2, 1]) == 3
    assert totalFruit([0, 1, 2, 2]) == 3

if __name__ == "__main__":
    test()

