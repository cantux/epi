def prev_less_element(arr):
    len_a = len(arr)
    s = []
    prev_arr = [-1] * len_a
    for i in range(len_a):
        while s and arr[s[-1]] > arr[i]:
            s.pop() 
        prev_arr[i] = s[-1] if s else -1
        s.append(i)
    return prev_arr

def next_less_element(arr):
    len_a = len(arr)
    s = []
    next_less = [-1] * len_a
    for i in range(len_a):
        while s and arr[s[-1]] > arr[i]:
            next_less[s.pop()] = i
        s.append(i)
    return next_less

def prev_larger_element(arr):
    s = []
    len_a = len(arr)
    prev_arr = [-1] * len_a

    for i in range(len_a):
        while s and arr[s[-1]] < arr[i]:
            s.pop() 
        prev_arr[i] = s[-1] if s else -1
        s.append(i)
    return prev_arr

def next_larger_element(arr):
    len_a = len(arr)
    s = []
    next_larger = [-1] * len_a
    for i in range(len_a):
        while s and arr[s[-1]] < arr[i]:
            next_larger[s.pop()] = i
        s.append(i)
    return next_larger

def test():
    print([3, 7, 8, 4])
    print("prev less: ", prev_less_element([3, 7, 8, 4]))
    print("next less: ", next_less_element([3, 7, 8, 4]))
    print([2, 9, 7, 8, 3, 4, 6, 1])
    print("prev less: ", prev_less_element([2, 9, 7, 8, 3, 4, 6, 1]))
    print("next less: ", next_less_element([2, 9, 7, 8, 3, 4, 6, 1]))
    print([3, 7, 8, 4])
    print("prev larger: ", prev_larger_element([3, 7, 8, 4]))
    print("next larger: ", next_larger_element([3, 7, 8, 4]))
    print([2, 9, 7, 8, 3, 4, 6, 1])
    print("prev larger: ", prev_larger_element([2, 9, 7, 8, 3, 4, 6, 1]))
    print("next larger: ", next_larger_element([2, 9, 7, 8, 3, 4, 6, 1]))

def prev_larger_element_print(arr):
    s = []
    len_a = len(arr)
    prev_arr = [-1] * len_a

    for i in range(len_a):
        print("start: ", s)
        while s and arr[s[-1]] < arr[i]:
            print("removing element: ", s.pop()) 
        print("before push: ", s)
        prev_arr[i] = s[-1] if s else -1
        s.append(i)
        print("after push: ", s)
    return prev_arr

def prev_less_element_print(arr):
    len_a = len(arr)
    s = []
    prev_arr = [-1] * len_a
    for i in range(len_a):
        print("stack before pops: ", s)
        while s and arr[s[-1]] > arr[i]:
            print("removing element: ", s.pop()) 
        print("stack after pops: ", s)
        prev_arr[i] = s[-1] if s else -1
        s.append(i)
        print("stack after push: ", s)
        print("prev_arr after: ", prev_arr)
    return prev_arr


if __name__ == "__main__":
    test()
