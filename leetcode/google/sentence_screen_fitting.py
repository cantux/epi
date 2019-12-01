#!/usr/bin/env python

    def wordsTyping(self, s, r_c, c_c):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        len_s = len(s)
        
        w_l = map(lambda x: len(x), s)
        print w_l
        
        dp = [0] * len_s
        
        for i in xrange(len_s):
            cursor = 0
            k = i
            while cursor < c_c:
                if cursor + w_l[k] > c_c:
                    break
                cursor += w_l[k] + 1
                k = (k + 1) % len_s
            dp[i] = k
        print dp
        total = r_c * c_c

def fnc():
    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

