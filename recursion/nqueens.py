    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        offsets = [(r, c) for r in [-1, 0, 1] for c in [-1, 0, 1]]
        def check_fit(r, c, sol):
            #diag
            for row_offset, col_offset in offsets:
                if not (row_offset == 0 and col_offset == 0):
                    curr_r, curr_c = r + row_offset, c + col_offset
                    while curr_r >= 0 and curr_c >= 0 and curr_c < n and curr_r < n:
                        if sol[curr_r][curr_c] == "Q":
                            return False
                        curr_r += row_offset
                        curr_c += col_offset
            return True

        def helper(curr_r, sol):
            if curr_r == n:
                ret.append(["".join(r) for r in sol])
                return
            for c in range(n):
                if check_fit(curr_r, c, sol):
                    sol[curr_r][c] = "Q"
                    helper(curr_r + 1, sol)
                    sol[curr_r][c] = "."

        curr_sol = [["." for c in range(n)] for r in range(n)]
        helper(0, curr_sol)
        return ret

