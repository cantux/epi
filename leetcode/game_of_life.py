def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    len_r = len(board)
    len_c = len(board[0])
    
    def within_boundry(r,c):
	return r >= 0 and c >= 0 and c < len_c and r< len_r
		    
    def apply_rules(real, copy, count, r, c):
       # Rule 1 or Rule 3        
	if copy[r][c] == 1 and (count < 2 or count > 3):
	    real[r][c] = 0
	# Rule 4
	if copy[r][c] == 0 and count == 3:
	    real[r][c] = 1
	
    
    copy_board = [[board[r][c] for c in xrange(len_c)] for r in xrange(len_r)]
    for r in xrange(len_r):
	for c in xrange(len_c):
	    count = 0
	    for i in xrange(-1, 2):
		for j in xrange(-1, 2):
		    if i == 0 and j == 0:
			continue
		    elif within_boundry(r + i, c + j):
			count += 1 if copy_board[r + i][c + j] else 0
	    apply_rules(board, copy_board, count, r, c)
    return board

def gameOfLifeinplace(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # Neighbors array to find 8 neighboring cells for a given cell
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

    rows = len(board)
    cols = len(board[0])

    # Iterate through board cell by cell.
    for row in range(rows):
	for col in range(cols):

	    # For each cell count the number of live neighbors.
	    live_neighbors = 0
	    for neighbor in neighbors:

		# row and column of the neighboring cell
		r = (row + neighbor[0])
		c = (col + neighbor[1])

		# Check the validity of the neighboring cell and if it was originally a live cell.
		if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
		    live_neighbors += 1

	    # Rule 1 or Rule 3
	    if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
		# -1 signifies the cell is now dead but originally was live.
		board[row][col] = -1
	    # Rule 4
	    if board[row][col] == 0 and live_neighbors == 3:
		# 2 signifies the cell is now live but was originally dead.
		board[row][col] = 2

    # Get the final representation for the newly updated board.
    for row in range(rows):
	for col in range(cols):
	    if board[row][col] > 0:
		board[row][col] = 1
	    else:
		board[row][col] = 0
