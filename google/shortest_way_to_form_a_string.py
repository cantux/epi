shortestWay(self, source, target):
    """
    :type source: str
    :type target: str
    :rtype: int
    """
    len_t = len(target)
    len_s = len(source)
    t_ptr, s_ptr = 0, 0
    count = 0
    while t_ptr < len_t:
        while s_ptr < len_s and t_ptr < len_t:
            if target[t_ptr] == source[s_ptr]:
                t_ptr += 1
            s_ptr += 1
        
        if t_ptr < len_t and target[t_ptr] not in source:
            return -1
        count += 1
        s_ptr = 0
        
        
    return count
