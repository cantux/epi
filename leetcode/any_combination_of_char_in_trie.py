ass Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word):
        curr_trie = self.trie
        for c in word:
            if c not in curr_trie:
                curr_trie[c] = {}
            curr_trie = curr_trie[c]
        curr_trie['#'] = {}
    
    @staticmethod
    def checkEnd(self, pt, ch):
        if c not in pt:
            return False
        return ("#" in pt[c])
    
    @staticmethod
    def getNextPt(pt, char):
        curr_trie = pt
        if char not in pt:
            return None        
        return pt[char]

class DLLNode:
    def __init__(self, val=None):
        self.prev = None
        self.nxt = None
        self.val = val
        
class DLL:
    def __init__(self):
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    @staticmethod
    def insert_prev(to, val):
        prev_el = to.prev
        new = DLLNode(val)
        prev_el.nxt = new
        to.prev = new
        new.prev = prev_el
        new.nxt = to
        
    def append(self, val):
        DLL.insert_prev(self.tail, val)
    
    @staticmethod
    def remove(node):
        prev = node.prev
        nxt = node.nxt
        prev.next = nxt
        nxt.prev = prev
        
class StreamChecker(object):
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for w in words:
            self.trie.insert(w)
        self.curr_active_pts = DLL()

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        found = False
        self.curr_active_pts.append(self.trie.trie)
        curr_el = self.curr_active_pts.head.nxt
        while curr_el is not self.curr_active_pts.tail:
            new = Trie.getNextPt(curr_el.val, letter)
            if not new:
                tmp = curr_el
                curr_el = curr_el.nxt
                DLL.remove(tmp)
            else:
                if '#' in new:
                    found = True
                curr_el.val = new
                curr_el = curr_el.nxt
            
        return found
