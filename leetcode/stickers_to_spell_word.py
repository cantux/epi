from collections import Counter

def minStickers(stickers, target):
    """
    :type stickers: List[str]
    :type target: str
    :rtype: int
    """
    # decomp
    # for argument's sake let's imagine a greedy path exists.
    # I will return -1 when I can't make progress anymore.
    
    t_c_dct = Counter(target)
    
    s_t_dct_lst = []
    for s in stickers:
        s_t_dct_lst.append(Counter(s))
            
    def get_char_count(counter_dct):
        res = 0
        for v in counter_dct.values():
            res += v
        return res
    
    def counter_dct_minus(counter_dct_left, counter_dct_right):
        for k, v in counter_dct_right.items():
            if k in counter_dct_left:
                if counter_dct_left[k] <= v:
                    del counter_dct_left[k]
                else:
                    counter_dct_left[k] -= v
    
    def counter_dct_minus_count(counter_dct_left, counter_dct_right, char_count):
        for k, v in counter_dct_right.items():
            if k in counter_dct_left:
                if counter_dct_left[k] < v:
                    char_count -= counter_dct_left[k]
                else:
                    char_count -= v
        return char_count            
    
    count = 0        
    while t_c_dct:
        current_char_count = get_char_count(t_c_dct)
        min_lst = []
        for i, s in enumerate(s_t_dct_lst):
            # check for each result, record as tuple of (result, idx)
            min_lst.append(( counter_dct_minus_count(t_c_dct, s, current_char_count), i))
        min_el = min(min_lst)
        print "min_lst: ", min_lst
        print "min_el: ", min_el
        if min_el[0] == current_char_count:
            return -1
        counter_dct_minus(t_c_dct, s_t_dct_lst[min_el[1]])
        count += 1
        print "target dct after remove: ", t_c_dct 
    return count


def test():
    assert minStickers(["with", "example", "science"], "thehat") == 3
    assert minStickers(["these","guess","about","garden","him"], "atomher") == 4

if __name__ == "__main__":
    test()
