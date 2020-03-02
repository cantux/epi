def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
	return 0
    len_r = len(matrix)
    len_c = len(matrix[0])
    
    max_found = 0
    
    for r in range(len_r):
	matrix[r][0] = int(matrix[r][0])
	if matrix[r][0] == 1:
	    max_found = 1
	    
    for c in range(len_c):
	matrix[0][c] = int(matrix[0][c])
	if matrix[0][c] == 1:
	    max_found = 1
    
    for r in range(1, len_r):
	for c in range(1, len_c):
	    if matrix[r][c] == "0":
		matrix[r][c] = 0
	    else:
		matrix[r][c] = min(matrix[r - 1][c -1], matrix[r - 1][c], matrix[r][c - 1]) + 1
		max_found = max(max_found, matrix[r][c])
		
    return max_found ** 2
