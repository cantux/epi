#!/usr/bin/env python

import random
import math

def gen_number(a, b):
    interval = b - a + 1
    num_bits = math.log(interval, 2)
    while True: 
        counter = num_bits
        i = 0
        while counter >= 0:
            i = (i << 1) | random.randint(0, 1)
            counter -= 1
        if i < interval:
            return i + a

def main():
    for i in range(30):
        print(gen_number(5, 10))

if __name__ == "__main__":
    main()
