import sys
# Complete the largestRectangle function below.
def largestRectangle(h):
    # what is the minimum among any certain ranges?
    # find mins first
    len_h = len(h)
    max_found = 0
    for i in range(len_h):
        curr_min = h[i]
        for j in range(i, len_h):
            curr_min = min(curr_min, h[j])
            max_found = max(max_found, curr_min * (j - i + 1))
    
    return max_found


