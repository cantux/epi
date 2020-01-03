def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    if not wordList: return 0
    if endWord not in wordList: return 0
    len_w = len(wordList[0])
    words = set(wordList) 
    chrs = [chr(i) for i in range(ord('a'), ord('z') + 1)]
	    
    min_l = sys.maxsize
    seen = set()
    q = deque([(beginWord, 1)]) # 0 if beginWord in wordList else 1)])
    while q:
	curr_w, curr_c = q.popleft()
	if curr_w not in seen:
	    seen.add(curr_w)
	    for i in xrange(len_w):
		first, last = curr_w[:i], curr_w[i + 1:]
		for c in chrs:
		    cand_w = first + c + last
		    if cand_w == endWord:
			return curr_c + 1
			# min_l = min(min_l, curr_c + 1)
		    elif cand_w in words: #wordList:
			q.append((cand_w, curr_c + 1))
    return 0 # if min_l == sys.maxsize else min_l
	
