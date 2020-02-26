
def has_two_sum(A, t):
    len_a = len(A)
    left, right = 0, len_a - 1
    while left <= right:
        curr = A[left] + A[right]
        if curr == t:
            return True
        elif curr < t:
            left += 1
        else:
            right -= 1
    return False

def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - a for a in A)
