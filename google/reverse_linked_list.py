reverse(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # I like to keep a reference to the previous
        # I will put curr into temp, make assignments to it then update
        if not head:
            return None
        
        prev = head
        curr = head.next
        prev.next = None
        # I want to decide how should I terminate this
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
