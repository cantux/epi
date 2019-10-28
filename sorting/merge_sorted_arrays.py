#!/usr/bin/env python
def fnc(top_arr, bot_arr):
    len_top, len_bot= len(top_arr) - len(bot_arr), len(bot_arr) 
    top, bot, write_idx = len_top - 1, len_bot - 1, len(top_arr) - 1
    
    while 0 <= top and 0 <= bot:
        curr_top = top_arr[top]
        curr_bot = bot_arr[bot]

        if curr_top > curr_bot:
            top_arr[write_idx] = curr_top
            top -= 1
        else:
            top_arr[write_idx] = curr_bot
            bot -= 1
        write_idx -= 1

    while 0 <= bot:
        top_arr[write_idx] = bot_arr[bot]
        write_idx -= 1
        bot -= 1

    return top_arr

def test():
    assert fnc([1, None], [2]) == [1, 2]
    assert fnc([2, None], [1]) == [1, 2]
    assert fnc([1, 2, None], [3]) == [1, 2, 3] 
    assert fnc([1, 3, None], [2]) == [1, 2, 3]
    assert fnc([1, None, None], [2, 3]) == [1, 2, 3]
    assert fnc([2, None, None], [1, 3]) == [1, 2, 3] 
    assert fnc([3, None, None], [1, 2]) == [1, 2, 3]
    

if __name__ == "__main__":
    test()

