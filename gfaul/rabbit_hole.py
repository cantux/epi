from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
  len_l = len(L)
  for i in range(len_l):
    L[i] -= 1
  prev = {}
  max_found = 0

  for i in range(len_l):
    if i not in prev: 
      tortoise = i
      hare = i
      while True:
        tortoise = L[tortoise]
        hare = L[L[hare]]
        if hare == tortoise:
          break
      tortoise = i
      while tortoise != hare:
        tortoise = L[tortoise]
        hare = L[hare]
      start_of_loop = tortoise
      
      loop_size = 1
      curr = L[start_of_loop]
      while curr != start_of_loop:
        loop_size += 1
        curr = L[curr]
      curr = L[start_of_loop]
      while curr != start_of_loop:
        prev[curr] = loop_size
        curr = L[curr]
      prev[start_of_loop] = loop_size
      print("prev: " + str(prev))
      if i != start_of_loop:
        path_size = 0
        curr = i
        while curr != start_of_loop:
          if curr in prev:
            path_size += prev[curr] - loop_size
            break
          curr = L[curr]
          path_size += 1
        print("path_size: " + str(path_size))
        curr = i
        while curr != start_of_loop and curr not in prev:
          prev[curr] = path_size + loop_size
          path_size -= 1
          curr = L[curr]
        print("prev after: " + str(prev))
    max_found = max(prev[i], max_found)
  return max_found

N = 5
L = [2, 4, 2, 2, 3]
print(getMaxVisitableWebpages(N, L))
