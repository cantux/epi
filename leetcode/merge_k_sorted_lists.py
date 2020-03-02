
#!/usr/bin/env python
import heapq

def fnc(lists):
    len_l = len(lists)
    res = ListNode(None)
    if not lists:
        return res.next
    
    hpq = []
    
    for l in lists:
        if l:
            heapq.heappush(hpq, (l.val, l))
        
    # what is the termination condition?
    # 
    curr = res
    while hpq:
        val, popped_node = heapq.heappop(hpq)
        curr.next = popped_node
        # if there is still a valid element in the list
        if popped_node.next:
            heapq.heappush(hpq, (popped_node.next.val, popped_node.next))
        
        popped_node.next = None
        curr = curr.next
    
    return res.next

def iter_mergeKLists(lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
	for i in range(0, amount - interval, interval * 2):
	    lists[i] = merge(lists[i], lists[i + interval])
	interval *= 2
    return lists[0] if amount > 0 else lists

def rec_mergeKLists(lists):
    if not lists:
        return 
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = mergeKLists(lists[:mid])
    r = mergeKLists(lists[mid:])
    return merge(l, r)

def merge(l, r):
    dummy = cur = ListNode(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

