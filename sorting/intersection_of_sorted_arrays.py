#!/usr/bin/env python

def fnc(top_arr, bot_arr):
    if not top_arr or not bot_arr: return []
    len_top, len_bot = len(top_arr), len(bot_arr)
    
    ret = []
    top, bot = 0, 0
    while top < len_top and bot < len_bot:
        curr_top = top_arr[top]
        curr_bot = bot_arr[bot]
        if curr_top == curr_bot and (not ret or ret[-1] != curr_top):
            
            ret.append(curr_top)
            top += 1
        elif curr_top > curr_bot:
            bot += 1
        else:
            top += 1

    return ret

def test():
    assert fnc(None, None) == []
    assert fnc([], []) == []
    assert fnc([], [1]) == []
    assert fnc([1], []) == []
    assert fnc([1], [1]) == [1]
    assert fnc([1], [1, 2]) == [1]
    assert fnc([1, 1], [1, 2]) == [1]
    assert fnc([1, 1], [1, 1, 2]) == [1]
    assert fnc([1, 1, 2], [1, 1, 2]) == [1, 2]
    

if __name__ == "__main__":
    test()

