


def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    mem = set()
    def rec(n):
        ret = []
        while n != 0:
            rem = n%10
            ret.append(rem)
            n = n // 10
        s = 0
        for r in ret:
            s += r ** 2
        if s == 1:
            return True
        elif s in mem:
            return False
        mem.add(s)
        return rec(s)
    
    return rec(n)
