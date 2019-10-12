#!/usr/bin/env python

# given n building with arbitrary number pf residents living in it
# place a lamp post such that the total walking distance of every individual is minimized.
# placing the lamp post at random k and l -> 
## 0.. k ... n -> a[0] * k + a[1] * k - 1 ... a[k] * 0 + a[k + 1] * 1 ... a[n - 1] * (n - k)
## find the total distances to k and l.
## 
### if k yields larger than l 
#### we know post should be closer to 

# super egg drop is similar to this
# there is a level k that the egg break
# and there is the level we are trying right now
import random
def min_dist(lst):
    len_lst = len(lst)
    k = random.randint(0, len_lst // 2)
    l = random.randint((len_lst // 2) + 1, len_lst - 1)

    return -1

def test():
    assert min_dist(None) == -1

if __name__ == "__main__":
  test()

