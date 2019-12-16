#!/usr/bin/env python

import pprint

def find_next_move():
    return None

class Game():
    def __init__(self):
        self.board = [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]
                ]
        (i, j) = comp_move()
        self.comp_first_move = (i, j)

    def make_move(self, i, j):
        self.board[i][j] = s
        if check_win() == 1:
            return pprint.pformat(self.board, indent=2) + "This shall never happen"
        elif check_win() == 0:
            return pprint.pformat(self.board, indent=2) + "Better luck next time"


        make_move(comp_move())
        if check_win() == 1:
            return pprint.pformat(self.board, indent=2) + "Bow before me"

        return pprint.pformat(self.board, indent=2)

    def check_win(self):
        return 1
        return 0
        
    
def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

