# it's easy to remember numbers as words,
# each digit on a keypad corresponds to letters.

# write a program that given any digits creates all the possible char sequences

# Brute
# for all digits encountered, create that many arrays.

# Let's create some test cases first.

# problem gets interesting with


# Since this is a tree like structure consider overlapping subproblems

keypad = {2: "ABC",
          3: "DEF",
          4: "GHI",
          5: "JKL",
          6: "MNO",
          7: "PQRS",
          8: "TUV",
          9: "XYZ"}

keypad_mp = {ch: key for (key, val) in keypad.items() for ch in val}

def seqs(nums, lst = [])
    # a b c
    # ad bd cd ae be ce af bf df
    curr = nums[0]
    chars = keypad[curr]
    new_lst = []
    for ch in chars:
        new_lst.append
    seqs(nums[1:], lst)
    
def test():
    assert 1 == 1
    seqs()

if __name__ == "__main__":
    test()
