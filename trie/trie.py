#!/usr/bin/env python
from collections import deque

class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.parent = None
        self.char = char
    
    def set_terminal(self):
        self.children["#"] = None
        
    def check_word(self):
        return "#" in self.children
    
    
class Trie:
    def __init__(self):
        self.head = TrieNode("$")
        
    def insert(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr.children:
                new = TrieNode(ch)
                curr.children[ch] = new
                new.parent = curr
            curr = curr.children[ch]
            
        curr.set_terminal()

    def search(self, word):
        curr = self.head
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return curr.check_word()

    def __repr__(self):
        res = ""
        q = deque([self.head])
        while q:
            curr = q.popleft()
            
            for child in curr.children.values():
                res += "curr.char: " + curr.char 
                if child: 
                    res += " child.char: " + child.char
                    q.append(child)
                res += "\n"
        return res


def test():
    trie = Trie()
    trie.insert("abc")

    print trie
    assert trie.search("abc") 
    trie.insert("ab")
    print trie
    assert trie.search("ab")
    assert not trie.search("b")
    assert not trie.search("a")

if __name__ == "__main__":
    test()

