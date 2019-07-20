def permute(arr):
    pass

def test():
    res = permute([1, 2, 3])
    t_list = []
    map(lambda x: t_list.append(x in [[1, 2, 3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]))
    assert all(t_list)
