def solve(board):
    row_dp = [0] * 9
    col_dp = [0] * 9
    box_dp = [0] * 9 # list of 9 values
    
    def get_box(r, c):
	return (r // 3) * 3 + (c // 3)
    
    def get_possible_vals(r,c):
	res = []
	for i in range(0, 9):
	    if not row_dp[r] >> i & 1 and not col_dp[c] >> i & 1 and not box_dp[get_box(r, c)] >> i & 1:
		res.append(i + 1)
	return res
    
    def comission_dp(r, c, val):
	bitval = 1 << (val - 1)
	row_dp[r] |= bitval
	col_dp[c] |= bitval
	box_dp[get_box(r, c)] |= bitval
    
    def all_one_single_zero(val):
	bitval = (1 << (9 - val + 1)) - 1
	bitval <<= val
	bitval |= (1 << (val - 1)) - 1
	return bitval
    
    def decomission_dp(r, c, val):
	bitval = all_one_single_zero(val)
	row_dp[r] &= bitval
	col_dp[c] &= bitval
	box_dp[get_box(r, c)] &= bitval
	
    for r in xrange(9):
	for c in xrange(9):
	    if board[r][c] == ".":
		board[r][c] = 0
	    else:
		board[r][c] = int(board[r][c])
    
    for r in xrange(9):
	for c in xrange(9):
	    if board[r][c] != 0:
		comission_dp(r, c, board[r][c])

    def bt(curr_row, curr_col):
	for r in xrange(curr_row, 9):
	    for c in xrange(curr_col, 9):
		if board[r][c] == 0:
                    possible_vals = get_possible_vals(r, c)
                    print r, c
                    print possible_vals
                    if not possible_vals:
                        return False
                    else:
                        for p_v in possible_vals:
                            board[r][c] = p_v
                            comission_dp(r, c, p_v)
                            if bt(r, c):
                                return True
                            else:
                                board[r][c] = 0
                                decomission_dp(r, c, p_v)
                        return False
	return False
			
    if not bt(0, 0):
        print "dam"

    
    for r in xrange(9):
	for c in xrange(9):
	    board[r][c] = str(board[r][c])

    print board

def test():
    case = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solve(case)

if __name__ == "__main__":
    test()
