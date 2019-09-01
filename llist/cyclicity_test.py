# decomp
# given a single list check if there is a cycle in it
# this may get clearer if we ahave a good dfiniton of a cycle
# a cycle is a node in the list refers to a previous node.
# since this is a single list we know for a fact that this cycle must be at the end.

# brute force is for everynode N, go over the whole list and check if we ever hit N again.
# the first time we hit N we will return true. if we don't and reach the end it's not a cycle.

# we could keep a set of nodes, and check if the neighbor is in that map. O(n) space complexity.

# a general trick with lists is to use a fast and a slow pointer. one jumping two nodes at a time.
# we must prove that if we used a fast and a slow pointer
# they will always be meeting if there is a cycle
# assume length of the whole list is N, number of nodes before the cycle begins is K and length of the cycle is L

# if N is odd:
# K is odd, L is even: fast ptr will be at (2K) modL when slow reached to Kth node. ShowK + i modK will ever
# K is even, L is odd
# elif N is even:
# K is odd, L is odd
# K is even L is even
