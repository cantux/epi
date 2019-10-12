
#!/usr/bin/env python
def fnc(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        proc = set(nums)
        
        found = 0
        
        while proc:
            curr = proc.pop()
            
            lower = 0
            a = curr - 1
            while a in proc:
                proc.remove(a)
                a -= 1
                lower += 1
                
            upper = 0
            b = curr + 1
            while b in proc:
                proc.remove(b)
                b += 1
                upper += 1
                
            found = max(found, upper + lower + 1)
        return found

def test():
    assert fnc([100,4,200,1,3,2]) == 4

if __name__ == "__main__":
    test()

