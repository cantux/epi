"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    if len(p) > len(s):
	return []
    
    counter = collections.defaultdict(lambda: 0)
    counter2 = collections.defaultdict(lambda: 0)
    
    for c in s[:len(p)]:
	counter[c] += 1
	
    for c in p:
	counter2[c] += 1
	
    def counter_match(c1, c2):
	for c in c2:
	    if c1[c] == c2[c]:
		continue
	    else:
		return False
	return True
    
    res = []
    
    if counter_match(counter, counter2):
	res.append(0)
	
    for i, c in enumerate(s[len(p):]):
	counter[s[i]] -= 1
	counter[c] += 1
	if counter_match(counter, counter2):
	    res.append(i + 1)
	    
    return res
