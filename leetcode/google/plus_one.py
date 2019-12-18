    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len_d = len(digits)
        ret = []
        carry = 1
        for d in digits[::-1]:
            curr = d + carry
            carry = curr // 10
            ret.append(curr % 10)
        
        if carry: ret.append(carry)
        return ret[::-1]
