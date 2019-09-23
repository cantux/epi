import math

def num_to_bin_str(i):
  out = list()
  while i != 0:
    out.append(str(int(i % 2)))
    i = math.floor(i / 2)
  return ''.join(list(reversed(out)))

print(num_to_bin_str(75))
