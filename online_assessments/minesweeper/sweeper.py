
import sys
from game import Game

def main():
    print("SWEEP THEM MINES SOLDIER!!")

    argc = len(sys.argv)
    row_c, col_c, bomb_c = 5, 5, 5
    if argc == 4:
        row_c = argv[1]
        col_c = argv[2]
        bomb_c = argv[3]

    g = Game(row_c, col_c, bomb_c)

    while g.get_state() == Game.CONTINUE:
        g.print_visible_board()
        row_move_str = input("Enter row num 1-{0}".format(row_c))
        col_move_str = input("Enter row num 1-{0}".format(col_c))
        g.make_move(row_move_str, col_move_str)
        g.print_board()
    
    if g.get_state() == Game.WIN:
        print("You live to fight another day!")
    else:
        print("Your service will be remembered")

    g.print_board()




if __name__ == "__main__":
    main()
