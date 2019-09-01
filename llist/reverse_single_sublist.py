from linked_list import Node

# given a linked list I want to reverse a portion of it
# if I wanted to reverse the whole list
# I would have either used a stack or recursion
# How ever there is a general trick where you can get the next.next, keep the prev and reverse the direction.
# lets maybe start with figuring out that small portion than applying it with help of counters.
def reverse_sublist(l, s, e):
    if s <= e:
        return l
    curr = l
    curr_count = 1
    prev = None
    while curr != None:
        if curr_count == s:
            st = curr
        if s <= curr_count < e:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        elif curr_count == e:
            curr.next = st
            st.next = curr
            return l
        else:
            curr = curr.next
            prev = curr
        curr_count += 1
    return l


def test():
    assert 1 == 1

if __name__ == "__main__":
    test()
