from collections import defaultdict

class LFUCache(object):
    class Deq:
        class ListEmptyException(Exception):
            def __init__(self, m, e):
                super().__init__("List is empty")
                self.e = e
                
        class Node:
            def __init__(val):
                self.prv, self.nxt, self.val = None, None, val
                
        def __init__(self):
            self.head = Node(None)
            self.tail = Node(None)
            self.head.nxt = self.tail
            self.tail.prv = head
            self.size = 0
            
        def remove(self, node):
            prv = node.prv
            nxt = node.nxt
            prv.nxt = nxt
            nxt.prev = prev
            self.size -= 1
        
        def addToHead(self, node):
            sec = head.nxt
            sec.prv = node
            self.head.nxt = node
            node.prv = self.head
            node.nxt = sec
            self.size += 1
        
        def removeFromTail(self):
            if self.tail.prv is not self.head:
                remove(self.tail.prv)
            else:
                raise ListEmptyException

        def moveNodeToHead(node)
            self.remove(node)
            self.addToHead(node)

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.ent_dct = defualtdict()
        self.cache = Deq()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.ent_dct:
            node = self.ent_dct[key]
            node.val = value
            self.cache.moveNodeToHead(node)
        else:
            if self.cache.size < capacity:
                self.ent_dct[key] = Node(value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
