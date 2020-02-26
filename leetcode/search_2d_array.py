    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        len_r = len(matrix)
        len_c = len(matrix[0])
        r = len_r - 1
        c = 0
        
        while c < len_c and r >= 0:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False
