#!/usr/bin/env python

def gasup(gallons, distances):
    # first of all, see that greedily choosing the city with the most gas doesn't necessarily allow you to make it through the whole loop
    # the accumulation of the gas has to stand the test of the next nodes
    # brute force is n**2, starting from each point, checking(wrap around if we can make it back without ever hitting 0 or below)
    # better with invariants, sort of like a line sweep
    
    remaining_gallons = 0
    city = 0

    num_cities = len(gallons)
    for i in range(1, num_cities):
            
    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

