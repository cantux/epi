import random

class Game:
    CONTINUE = 1
    WIN = 2
    LOSE = 3
    def __init__(self, row_c, col_c, bomb_c, seed=None):
        self.state = Game.CONTINUE
        self.row_c, self.col_c = row_c, col_c
        self.board = [['.' for _ in range(col_c)] for _ in range(row_c)]
        self.visible_board = [['H' for _ in range(col_c)] for _ in range(row_c)]
        self.move_count = 0
        self.bomb_c = bomb_c
        self.win_con = (row_c * col_c) - bomb_c
        if seed:
            self.random = random.seed(seed)
        else:
            self.random = random
    def get_state(self):
        return self.state


    def print_board(self):
        print("DEBUG BOARD")
        print("   " + "".join([" " + str(i + 1).rjust(2) for i in range(self.col_c)]))
        for i in range(self.row_c):
            print(str(i + 1).rjust(2) + " " + " ".join([x + " " for x in self.board[i]]))
        
    def print_visible_board(self):
        print("VISIBLE BOARD")
        print("   " + "".join([" " + str(i + 1).rjust(2) for i in range(self.col_c)]))
        for i in range(self.row_c):
            print(str(i + 1).rjust(2) + " " + " ".join([x + " " for x in self.visible_board[i]]))
 
    def make_move(self, row_move_str, col_move_str):
        row_move = int(row_move_str) - 1
        col_move = int(col_move_str) - 1
        if self.move_count == 0:
            self.win_con = self.gen_board(row_move, col_move)

        curr_spot = self.board[row_move][col_move]
        if curr_spot == "*":
            self.state = Game.LOSE
        elif curr_spot == ".":
            self.flood_fill(row_move, col_move, set())
        else:
            self.visible_board[row_move][col_move] = self.board[row_move][col_move]
            self.move_count += 1

        # check win con
        if self.win_con == self.move_count:
            self.state = Game.WIN
    
    def gen_board(self, row_move, col_move):
        bombs = self.random.sample(range(self.row_c * self.col_c), self.bomb_c)
        bomb_indeces = [(b // self.row_c, b % self.col_c) for b in bombs]
        for r_b, c_b in bomb_indeces:
            self.board[r_b][c_b] = "*"
            for r_o in [-1, 0, 1]:
                for c_o in [-1, 0, 1]:
                    if not (r_o == 0 and c_o == 0):
                        curr_r, curr_c = r_b + r_o, c_b + c_o
                        if self.check_within(curr_r, curr_c):
                            if self.board[curr_r][curr_c] == ".":
                                self.board[curr_r][curr_c] = "1"
                            elif self.board[curr_r][curr_c] != "*":
                                self.board[curr_r][curr_c] = str(int(self.board[curr_r][curr_c]) + 1)


    def check_within(self, row_move, col_move):
        if row_move >= 0 and row_move < self.row_c and col_move >= 0 and col_move < self.col_c:
            return True
        return False

    def get_r_c_key(self, r, c):
        return str(str(r) + " " + str(c))

    def flood_fill(self, row_move, col_move, seen):
        curr_key = self.get_r_c_key(row_move, col_move)
        if self.check_within(row_move, col_move) and curr_key not in seen:
            seen.add(curr_key)
            if self.board[row_move][col_move] == ".":
                self.visible_board[row_move][col_move] = "."
                self.move_count += 1
                for r_o, c_o in [(-1, 0),(0, -1), (1, 0), (0, 1)]:
                    self.flood_fill(row_move + r_o, col_move + c_o, seen) 
