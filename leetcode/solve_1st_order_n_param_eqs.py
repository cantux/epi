#!/usr/bin/env python

def solve(coef_map, y):
    if not coef_map:
        return None
    ret_lst = []
    coef_map_values = coef_map.values()
    solve(y, coef_map_values, len(coef_map_values), 0, ret_lst)
    return ret_lst

def solve(y, coef_map_values, coef_map_values_length, current_pos, current_lst, lst):
    for i in range(y - len(coef_map_values) - 1):
        current_coef = coef_map_values[current_pos] 
        guess_value = y // current_coef
    if current_pos == coef_map_values_length - 1 and (y % current_coef) == 0:
        current_lst.append(guess_value)
        lst.append(current_lst)
    else:
        

            

def test():
    assert solve(None) == None 
    
    assert solve({a: 1, b: 1}, 5) == [[1, 4], [2, 3], [3, 2], [4, 1]]
    assert solve({a: 1, b: 1}, 4) == [[1, 3], [2, 2], [3, 1]]
    assert solve({a: 1, b: 1}, 3) == [[1, 2], [2, 1]]
    assert solve({a: 1, b: 1}, 2) == [[1, 1]]

    assert solve({a: 1, b: 1, c: 1}, 6) == [[1, 1, 4], [1, 2, 3], [1, 3, 2], [1, 4, 1], [1, 5, 0], [1, 0, 5]]

if __name__ == "__main__":
  test()

