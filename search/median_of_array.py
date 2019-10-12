
#!/usr/bin/env python
from find_kth_largest import part_kth

def median(lst):
# decomp
# given an unsorted list find the median
# median { len even: arr[len //2] + arr[len //2 +1] * 0.5
# { len odd arr[len // 2 + 1]
    len_lst = len(lst)
    if len_lst % 2 == 0:
        return (part_kth(lst, len_lst // 2) + part_kth(lst, (len_lst // 2) + 1)) * 0.5
    return part_kth(lst, (len_lst // 2) + 1)

import random
def shuffle(lst):
    i = 0
    for i in range(len(lst)):
        pos = random.randint(i, len(lst) - 1)
        lst[i], lst[pos] = lst[pos], lst[i]
 
def test():
    lst = range(10)
    for _ in range(100):
        shuffle(lst)
        assert median(lst) == 4.5

if __name__ == "__main__":
    test()

