
from collections import Counter
import copy

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    
    # p's anagrams in s
    # find all of them and return in a list
    
    # brute force
    # create all anagrams of p
    # go over s char by char
    
    # I think we can apply sliding window of length len(p)
    # create frequency map and update the map with each 
    # character removal and addition to the front.
    
    
    # infra
    p_len = len(p)
    s_len = len(s)
    
    # create the freq map
    p_freq_map = Counter(p)
    p_max_map = copy.deepcopy(p_freq_map)
    
    for i in range(len(p)):
        curr_s = s[i]
        if curr_s in p_freq_map:
            p_freq_map[curr_s] -= 1
    ret = []

    start_cursor = 0
    end_cursor = len(p)
    while end_cursor < len(s):
        if all(map(lambda x: x == 0, p_freq_map.values())): # reduce(lambda p, n: p == n == 0, p_freq_map.values()):
            ret.append(start_cursor) # optimize with a deq or LL

        s_start = s[start_cursor]
        if s_start in p_freq_map:
            p_freq_map[s_start] += 1
            
        s_end = s[end_cursor]
        if s_end in p_freq_map:
            p_freq_map[s_end] -= 1
            
        end_cursor += 1
        start_cursor += 1
    
    return ret

def find_anagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    p_len = len(p)
    s_len = len(s)
    if not p_len or not s_len: return []
    if p_len > s_len: return []
    
    p_freq_map = Counter(p)
    p_max_map = copy.deepcopy(p_freq_map)
    item_left_count = p_len
    for i in range(p_len):
        curr_s = s[i]
        if curr_s in p_freq_map:
            p_freq_map[curr_s] -= 1
            if p_freq_map[curr_s] >= 0:
                item_left_count -= 1
    ret = []

    if item_left_count == 0:
        ret.append(0) 
   
    start_cursor = 0
    end_cursor = len(p)
    while end_cursor < len(s):
        s_start = s[start_cursor]
        if s_start in p_freq_map:
            if p_freq_map[s_start] >= 0:
                item_left_count += 1
            p_freq_map[s_start] += 1

        s_end = s[end_cursor]
        if s_end in p_freq_map:
            p_freq_map[s_end] -= 1
            if p_freq_map[s_end] >= 0:
                item_left_count -= 1
        
        start_cursor += 1
        end_cursor += 1

        if item_left_count == 0:
            ret.append(start_cursor)
    return ret

def test():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6] 

if __name__ == "__main__":
    test()
