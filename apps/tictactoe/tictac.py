class TicTacToe:
    diagonals = [
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
            ]
    
    verticals = []
    for c in range(3):
        verticals.append([(0, c), (1, c), (2, c)]) 

    horizontals = []
    for r in range(3):
        horizontals.append([(r, 0), (r, 1), (r, 2)])

    wins = verticals + diagonals + horizontals

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.curr_turn = "o"
        self.opp_turn = "x"

    def toggle_turn(self):
        self.curr_turn, self.opp_turn = self.opp_turn, self.curr_turn

    def place_token(self, pos_r, pos_c):
        if self.board[pos_r][pos_c] == " ":
            self.board[pos_r][pos_c] = self.curr_turn
            return True
        return False

    def check_win(self):
               
        for w in TicTacToe.wins:
            winner = True
            for r,c in w:
                winner = winner and self.board[r][c] == self.curr_turn
            if winner:
                return True
        return False
   
    
    def print_board(self): 
        print self.board

    def ai_move(self):
        # curr_turn: based on whose turn it is, ai shall try to maximize it
        # I think idea here is to find a move that minimizes the winning chances of the opponent while maximizing yours.
        # we could come up with a scoring system where if opponent wins you get a -1 and if you win you get +1 and 0 on draws
        # here is a problem I can think of such a scoring system: if the recursion tree is deeper we will get smaller or larger values.
        # I feel we shouldn't propogate sum of the values but win percentages only the current level
        pass
        
def test():
    play_with = ""
    while True:
        print "choose 1: human or ai"
        play_with = raw_input()
        if play_with in ["ai", "human"]:
            break

    if play_with == "human":
        ttt = TicTacToe()
        while True:
            ttt.toggle_turn()
            while True:
                print "place token to R(space)C: "
                inp = raw_input()
                try:
                    r, c = inp.split(" ")
                except:
                    continue
                if ttt.place_token(int(r), int(c)):
                    break
            print ttt.print_board()
            if ttt.check_win():
                break

        print "winner winner chicken dinner"
    elif play_with == "ai":
        pass 
if __name__ == "__main__":
    test()

