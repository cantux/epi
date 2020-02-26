# Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.


def fnc(T):
    # wait until a warmer temprature T[j] > T[i] s.t j > i --->> find j - i, for all i

    # simply find next greater element
    len_t = len(T)
    s = []
    res = [0] * len_t
    # imagine we fill the stack
    # with every element we encounter, we update the previous elements that are in the stack that are smaller than it
    # and we remove the previous elements so we don't have to update them again
    for i in range(len_t):
        while s and T[i] > T[s[-1]]:
            el = s.pop()
            res[el] = i - el
        s.append(i)
    return res


def test():
    fnc([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert 0 == 1, "Success"


if __name__ == "__main__":
    test()