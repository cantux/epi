def lls(s):
    """
    :type s: str
    :rtype: int
    """
    left, right = 0, 0
    len_s = len(s)
    max_found = 0
    wd = set()
    while right < len_s:
        # move right until we hit a char that appeared before
        while right < len_s and s[right] not in wd:
            wd.add(s[right])
            right += 1
        
        max_found = max(max_found, right - left)
        if right < len_s:
            while left < len_s and s[right] in wd:
                wd.remove(s[left])
                left += 1
        # save the length 4 - 1
        # then move left until that particular char is removed from the list 
            # 0a 1b 2c 3d 4b ->  right == 4 -> move left until 2(b is removed) which is b's location + 1
        
    
    return max_found

