# a programmer mistakenly deleted .'s between ip addresses
# write a program that returns a list of possible ip address from a given string

# partition given str into 4 parts.

# we can check the left-over size once we partition once.

# we have overlapping sub problems so we should build the problem instead of using recursion.

def gen_ips(text):
    # try to move the separators
    for i in range(3):
        first = int(text[:i])
        if first < 256:
            for j in range(3):
                second = int(text[i:i+j])
                if second < 256:
                    for k in range(3):
                        third = int(text[i + j: i + j + k])
                        if balbalbal


def test():
    assert 1 == 1

if __name__ == "__main__":
    test()
