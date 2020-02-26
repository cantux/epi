# what's the high level going to look like?

class Checkers:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.current_turn = 1
        self.opposing_turn = 2
        
        # setup board
        for i in range(8)[1::2]:
            self.board[0][i] = 1
        for i in range(8)[::2]:
            self.board[1][i] = 1
        for i in range(8)[1::2]:
            self.board[2][i] = 1

        for i in range(8)[::2]:
            self.board[7][i] = 2
        for i in range(8)[1::2]:
            self.board[6][i] = 2
        for i in range(8)[::2]:
            self.board[5][i] = 2

    def toggle_turn():
        self.current_turn, self.opposing_turn = self.opposing_turn, self.current_turn
    


def play(checkers):
    checkers = Checkers()
    checkers.set_current_turn(0)
    while checkers.winning_condition(): # returns False
        inp = raw_input()
        piece_pos_x, piece_pos_y, new_piece_pos_x, new_piece_pos_y = inp.split(" ") # direction: [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        while checkers.make_move(current_turn, piece_pos_x, piece_pos_y, (new_piece_pos_x, new_piece_pos_y)):
            inp = raw_input()
            piece_pos_x, piece_pos_y, new_piece_pos_x, new_piece_pos_y = inp.split(" ")

    checkers.toggle_turn()


