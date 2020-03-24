def shortestToChar(self, S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    # shortest distance from a given character

    n = len(S)
    res = [sys.maxsize] * n
    for i, ch in enumerate(S):
        if ch == C:
            res[i] = 0

    for i in range(n - 1):
        if res[i] != sys.maxsize:
            res[i + 1] = min(res[i + 1], res[i] + 1)

    for i in reversed(range(1, n)):
        res[i - 1] = min(res[i - 1], res[i] + 1)

    return res;