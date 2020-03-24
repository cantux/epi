#!/usr/bin/env python

def word_search(board, words): 
    if not board: 
	return []
    
    trie = {"$" : {}} # {$: {a: {b: #, c:#}}}   ab, ac
    for w in words:
	curr_node = trie["$"]
	for ch in w:
	    if ch not in curr_node:
		curr_node[ch] = {}
	    curr_node = curr_node[ch]
	curr_node["#"] = None
	
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    res = []
    def dfs(curr_r, curr_c, curr_trie_node, word, visited):
	if (curr_r, curr_c) not in visited:
	    visited.add((curr_r, curr_c))
	    if "#" in curr_trie_node and word not in res:
		res.append(word)
	    if 0 <= curr_r < len_r and 0 <= curr_c < len_c and board[curr_r][curr_c] in curr_trie_node:
		for d_x, d_y in dirs:
		    dfs(curr_r + d_x, curr_c + d_y, curr_trie_node[board[curr_r][curr_c]], word + board[curr_r][curr_c], visited)
	    visited.remove((curr_r, curr_c))
		
    len_r, len_c = len(board), len(board[0])
    for r in range(len_r):
	for c in range(len_c):
	    visited = set()
	    dfs(r, c, trie["$"], "", visited)
	    
    return res 

def test():
    assert word_search([["a","a"]], ["aaa"]) == []
    assert all(w in ["oath", "eat"] for w in word_search([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
	

if __name__ == "__main__":
    test()

