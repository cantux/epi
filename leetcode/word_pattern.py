from collections import defaultdict

# given a pattern "abab" and given a list of words "cat dog cat dog" find if pattern is followed
def wordPattern(self, pattern: str, str: str) -> bool:
    p_d = defaultdict(list)
    
    for i, p in enumerate(pattern):
        p_d[p].append(i)
        
    str_l = str.split(" ")
    if len(str_l) != len(pattern):
        return False
    
    s_d = defaultdict(list)
    for i, w in enumerate(str_l):
        s_d[w].append(i)
    
    start_indeces_dct = {}
    for i, p in enumerate(pattern):
        if p not in start_indeces_dct:
            start_indeces_dct[p] = i
            
    for p, idx in start_indeces_dct.items():
        if p_d[p] != s_d[str_l[idx]]:
            return False
        
    return True

def wordPattern(self, pattern: str, str: str) -> bool:
    s_lst = str.split(" ")
    if len(s_lst) != len(pattern):
	return False
    d = {}
    d_r = {}
    for p,s in zip(pattern, s_lst):
	if p not in d:
	    d[p] = s
	    if s not in d_r:
		d_r[s] = p
	    else:
		return False
	elif d[p] != s:
	    return False
	elif d[p] == s and d_r[s] != p:
	    return False
    return True
