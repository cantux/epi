#!/usr/bin/env python
import pprint

class Board:
    def __init__(self, line=3):
        self.board = [["-" for _ in range(line)] for _ in range(line)]

    def __repr__(self):
        s = "* 0 1 2\n"
        for r_i, r in enumerate(self.board):
            s += str(r_i) + " "
            for c in r:
                s += c + " "
            s += "\n"
        return s

    def place_checker(self, r, c, token):
        self.board[r][c] = token

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.checkers = ["x", "-", "o"]
        self.current_turn = -1
        self.player1 = player1
        self.player2 = player2
        self.moves = [(-1, -1)]
    
    def start(self):
        while self.check_win_con(self.board):
            print self.board
            move = (-1, -1)
            while move in self.moves or len(move) != 2:
                print "enter a move that is not already played"
                if self.current_turn == -1:
                    move = self.player1.get_move()
                else:
                    move = self.player2.get_move()

            self.moves.append(move)
            self.board.place_checker(move[0], move[1], self.checkers[self.current_turn + 1])
            self.current_turn = self.current_turn * -1

    def check_win_con(self, board):
        return len(self.moves) != 10

class Player:
    def __init__(self, is_computer=False):
        self.is_computer = is_computer

    def get_move(self):
        if self.is_computer:
            return self.place_computer_checker()
        return self.ask_user_to_input_checker()

    def place_computer_checker(self):
        print "enter for computer" 
        return self.ask_user_to_input_checker()

    def ask_user_to_input_checker(self):
        # get inp
        return get_inp(lambda x:x[0] not in range(0,3) and x[1] not in range(0, 3),
                (-1, -1),
                "enter two integers with a space between them",
                lambda x: tuple(map(int, x.split(" "))),
                "ex entry: 1 2 or 0 0")

def get_inp(sentinel_exp, sentinel_init, prompt, conv_exp, conv_err_msg):
    var = sentinel_init 
    while sentinel_exp(var):
        var_str = raw_input(prompt)
        try:
            var = conv_exp(var_str)
        except Exception as e:
            print conv_err_msg + ": " + str(e)

    return var

def test():
    # take game properties
# is it a pvc or pvp
    # let's start with pvc
# see if the player want's to be x or o
    which_checker = get_inp(
            lambda x: x != 1 and x != 2, 
            -1, 
            "Enter 1 for x or 2 for o: ", 
            lambda x: int(x), 
            "enter an integer")
    if which_checker == 1:
        p1 = Player()
        p2 = Player(True)
    else:
        p1 = Player(True)
        p2 = Player()

    g = Game(p1, p2)

    g.start()    


# test with cvc

if __name__ == "__main__":
    test()

