# decompose
# starting from the first character, go up, go down down, go up up up, go down down down...

# sample test cases
# function signature
# brute force solution
# dry run
# more test cases
# better solution
# more test cases
# dry run test case
# implement
# debug

def sinus_p(text):
    first, second, third = [], [], []
    for i, c in enumerate(text):
        rem = i % 4
        if rem == 0 or rem == 2:
            second.append(c)
            first.append(' ')
            third.append(' ') 
        elif rem == 1:
            first.append(c)
            second.append(' ')
            third.append(' ')
        else:
            third.append(c)
            second.append(' ')
            first. append(' ')

    print first
    print second
    print third


def test():
    sinus_p('hello world')

if __name__ == "__main__":
    test()
