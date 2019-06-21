import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
        # go over the list
            # add two numbers
            # find the carry, starting carry is 0
            # create an entry for the last carry
        # keep a reference to head and return it
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = ListNode(0)
        current = head
        carry = 0
        print 'current List: ', listToStr(head)
        while l1 != None and l2 != None:
            sum_vals = l1.val + l2.val + carry
            act = sum_vals % 10
            carry = int(math.floor(sum_vals / 10))
            current.val = int(act)
            current.next = ListNode(0)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        print 'list after add: ', listToStr(head)
        if l1 != None:
            print 'here 0'
            if carry != 0:
                current.next.val = carry + l1.val
                current.next.next = l1.next
            else:
                current.next = l1.next
        elif l2 != None:
            print 'here 1'
            if carry != 0:
                current.next.val = carry + l2.val
                current.next.next = l2.next
            else:
                current.next = l2.next
        else:
            print 'here 2'
            current = None
        print 'list after all: ', listToStr(head)
        return head.next

def listToStr(lst):
    current = lst
    text = ''
    while current != None:
        text += str(current.val)
        current = current.next
    return text

def listToInt(l1):
    current = l1
    count = 1
    num = 0
    while current != None:
        num += count * current.val
        count *= 10
        current = current.next
    return num

def test():
    l1Head = ListNode(2)
    l1Head.next = ListNode(4)
    l1Head.next.next = ListNode(3)
    l2Head = ListNode(5)
    l2Head.next = ListNode(6)
    l2Head.next.next = ListNode(4)
    
    assert listToInt(addTwoNumbers(l1Head, l2Head)) == 807
    

if __name__ == "__main__":
    test()
