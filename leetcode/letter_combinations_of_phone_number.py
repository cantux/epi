    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        # adg
        # adh
        # adi
        # aeg
        # aeh
        # aei
        if not digits:
            return []
        len_d = len(digits)
        res = []
        
        def rec(curr_idx, curr_str):
            if curr_idx == len_d:
                res.append(curr_str)
                return
            
            for ch in dct[digits[curr_idx]]:
                rec(curr_idx + 1, curr_str + ch)
        
        rec(0, "")
        return res
