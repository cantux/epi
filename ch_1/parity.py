#!/usr/bin/env python


def brute_parity(x):
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res


def zarif_parity(x):
    res = 0
    while x:
        res ^= 1
        x &= x - 1
    return res

parity_cache = []
for i in range(2**16 - 1):
    parity_cache.append(zarif_parity(i))


def parity_cache_check(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (parity_cache[x >> (3 * mask_size)] ^
            parity_cache[x >> (2 * mask_size)] ^
            parity_cache[x >> (1 * mask_size)] ^
            parity_cache[x >> (0 * mask_size)])


def folding_parity(x):
   x ^= x >> 32 
   x ^= x >> 16 
   x ^= x >> 8 
   x ^= x >> 4 
   x ^= x >> 2 
   x ^= x >> 1
   return x & 0x1
if __name__ == "__main__":
    print(brute_parity(5))
    print(brute_parity(4))

    print(zarif_parity(5))
    print(zarif_parity(4))

    print(parity_cache_check(5))
    print(parity_cache_check(4))

    print(folding_parity(5))
    print(folding_parity(4))
