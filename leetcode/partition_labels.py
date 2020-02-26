
#!/usr/bin/env python

def fnc():
    dct_ch_start_end = {}
    for i, ch in enumerate(S):
	if ch not in dct_ch_start_end:
	    dct_ch_start_end[ch] = [i, i]
	else:
	    dct_ch_start_end[ch][1] = i
    
    unmerged_intervals = sorted(dct_ch_start_end.values(), key=lambda x: x[0])
    
    len_i = len(unmerged_intervals)
    
    res = [unmerged_intervals[0][1]]
    for i in range(1, len_i):
	if res[-1] > unmerged_intervals[i][0]:
	    res[-1] = max(unmerged_intervals[i][1], res[-1])
	else:
	    res.append(unmerged_intervals[i][1])
    
    curr_sum = res[0]
    for i in range(1, len(res)):
	res[i] -= curr_sum
	curr_sum += res[i]
    res[0] += 1         
    return res
def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

