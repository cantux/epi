def adv(arr):
    furthest_reach, last = 0, len(arr) - 1
    i = 0
    while i < furthest_reach and furthest_reach < last:
        furthest_reach = max(furthest_reach, a[i] + i)
        i += 1
    return furthest_reach >= last

def test():
    assert adv([1])
    assert adv([2])
    assert adv([1, 1])
    assert adv([2, 0])
    assert not adv([2, 0, 0])
    assert adv([2, 0, 1])
    assert not adv([0, 1, 1, 1, 1, 1])
    assert not adv([1, 1, 1, 0, 1, 1])

if __name__ == "__main__":
    test()
