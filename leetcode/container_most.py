def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    length = len(height)
    max_con = -sys.maxsize-1
    
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length: 
            max_con = max(max_con, min(height[i], height[j]) * (j - i))                
            j += 1
        i += 1   
    return max_con

def maxArea(height):
    maxarea = 0, l = 0, r = len(height) - 1;
    while (l < r): 
        maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
        if (height[l] < height[r])
            l += 1
        else
            r -= 1
    
    return maxarea

def test():
    assert 1 == 1

if __name__ == "__main__":
    test()
