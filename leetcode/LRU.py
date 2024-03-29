class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)



class DLLNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)

# Let's have em with phantom nodes.
class DubLyList:
    def __init__(self):
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __str__(self):
        current = self.head.next
        text = ""
        while current.next is not self.tail:
            text += str(current.value)
            current = current.next
        return text

class LRUCache:            
    def __init__(self, capacity):
        self.cache_dct = {} # {key: DLLNode}
        self.cache_lst = DubLyList()
        self.capacity = capacity
        self.count = 0
    
    # def _print(self):        
    #     print self.cache_lst
    #     print [str(k) + ": " + str(v) for (k,v) in self.cache_dct.items()]

    def get(self, key):
        if key in self.cache_dct:
            # move the node to head
            current = self.cache_dct[key]
            
                # pluck it out first
            prev = current.prev
            nxt = current.next
            prev.next = nxt
            nxt.prev = prev
                # place it to the head
            head = self.cache_lst.head
            current.prev = head
            head.next.prev = current
            current.next = head.next
            head.next = current
            
        return self.cache_dct[key].value if key in self.cache_dct else -1

    def put(self, key, value):
        # if key is already in cache update it and move to head
        if key in self.cache_dct:
            # set new value and move to head 
            # or 
            # remove and re-add it
            
            # remove it for interview purposes
            # cuz it saves code but other is faster
            current = self.cache_dct[key]
            current.next.prev = current.prev
            current.prev.next = current.next
        else:
            if self.count == self.capacity:
                # evict tail and add new one to head
                tail = self.cache_lst.tail
                self.cache_dct.pop(tail.prev.key)
                tail.prev.prev.next = tail
                tail.prev = tail.prev.prev
            else:
                self.count += 1
        # add new one to head and inc count
        new = DLLNode(key, value)
        self.cache_dct.update({key: new})
        head = self.cache_lst.head
        head.next.prev = new
        new.next = head.next
        head.next = new
        new.prev = head

def test():
    cache = LRUCache(2)
    cache.put(1, 1);
    cache._print()
    cache.put(2, 2);
    cache._print()
    print 'returns 1: ', cache.get(1);       # returns 1
    cache._print()
    print 'evicts key 2: ', cache.put(3, 3);    # evicts key 2
    cache._print()
    print 'returns -1: ', cache.get(2);       # returns -1 (not found)
    cache._print()
    print 'evicts key 1: ', cache.put(4, 4);    # evicts key 1
    cache._print()
    print 'returns -1: ', cache.get(1);       # returns -1 (not found)
    cache._print()
    print 'returns 3: ', cache.get(3);       # returns 3
    cache._print()
    print 'returns 4: ', cache.get(4);       # returns 4
    cache._print()
    

if __name__ == "__main__":
    test()
