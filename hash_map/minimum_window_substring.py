#!/usr/bin/env python

from collections import Counter
import sys
def fnc(self, s, t):
            freq_map = Counter(t)
        len_s = len(s)
        item_left = len(t)
        if len_s < item_left: return ""
        
        start = 0
        
        min_len = sys.maxsize
        found_start, found_end = -1, -1

        for end, end_item in enumerate(s):             
            if end_item in freq_map:
                item_left -= freq_map[end_item] > 0 
                freq_map[end_item] -= 1
            
            while item_left == 0:
                curr_window_size = end - start
                if (found_start, found_end) == (-1, -1) or curr_window_size < min_len:
                    min_len = curr_window_size
                    found_start, found_end = start, end 

                curr_start = s[start]
                if curr_start in freq_map:
                    freq_map[curr_start] += 1
                    item_left += freq_map[curr_start] > 0 
                start += 1
                
        return s[found_start:found_end+1]

def test():
    assert fnc("ADOBECODEBANC", "ABC") == "BANC"

if __name__ == "__main__":
    test()

