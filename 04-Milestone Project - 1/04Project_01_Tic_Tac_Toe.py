# Project description:
# Create a Tic Tac Toe game. You are free to use any IDE you like.
#
# Here are the requirements:
#
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board


# The work flow:
# Ask input
# Check input (find number)
# Add input
# Show board
# Check win
# Check move (find blank)
# from IPython.display import clear_output# Global variables


def show_board(v_p, v_g):
    # clear_output()
    print('\n' * 100)
    print(" Available\t Game board\n positions\t  display!\n")
    print(f" {v_p['p7']} | {v_p['p8']} | {v_p['p9']} \t  {v_g['g7']} | {v_g['g8']} | {v_g['g9']}")
    print("-----------\t -----------")
    print(f" {v_p['p4']} | {v_p['p5']} | {v_p['p6']} \t  {v_g['g4']} | {v_g['g5']} | {v_g['g6']}")
    print("-----------\t -----------")
    print(f" {v_p['p1']} | {v_p['p2']} | {v_p['p3']} \t  {v_g['g1']} | {v_g['g2']} | {v_g['g3']}")


def initiate_game(preset):
    p1symbol = input("\nPlayer 1, Pick X or O and press enter: ")
    if 'X' in p1symbol.upper():
        preset.pop(-1)
    elif 'O' in p1symbol.upper():
        preset.pop(0)
    else:
        # clear_output()
        print('\n' * 100)
        print("\n\nWrong input!")
        initiate_game(preset)
    return preset


def use_input(loc, symbols, v_p, v_g):
    inp = int(input(f"Player {(loc % 2 != 0) + 1} ({symbols[loc]}), please enter your next position: "))
    if inp in v_p.values():
        pKey = 'p' + str(inp)
        gKey = 'g' + str(inp)
        v_p[pKey] = ' '
        v_g[gKey] = symbols[loc]
        show_board(v_p, v_g)
    else:
        print('\n\nWrong Input! Try again!')
        use_input(loc, symbols, v_p, v_g)


def check_win(vg):
    return (vg['g1'] == vg['g2'] == vg['g3'] != ' ') or (vg['g4'] == vg['g5'] == vg['g6'] != ' ') or (
            vg['g7'] == vg['g8'] == vg['g9'] != ' ') or (vg['g1'] == vg['g4'] == vg['g7'] != ' ') or (
                   vg['g2'] == vg['g5'] == vg['g8'] != ' ') or (vg['g3'] == vg['g6'] == vg['g9'] != ' ') or (
                   vg['g1'] == vg['g5'] == vg['g9'] != ' ') or (vg['g3'] == vg['g5'] == vg['g7'] != ' ')


def check_move(vg):
    return ' ' in vg.values()


def replay():
    return input('Play again? Enter Yes or No: ').lower().startswith('y')


while True:
    # clear_output()
    print('\n' * 100)
    print("Welcome to Tic Tac Toe!")

    # Declare variables
    positionboard = {'p1': 1, 'p2': 2, 'p3': 3, 'p4': 4, 'p5': 5, 'p6': 6, 'p7': 7, 'p8': 8, 'p9': 9}
    gameboard = {'g1': ' ', 'g2': ' ', 'g3': ' ', 'g4': ' ', 'g5': ' ', 'g6': ' ', 'g7': ' ', 'g8': ' ', 'g9': ' '}
    moveset = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']

    turns = initiate_game(moveset)  # all 9 moves in a sequence depending on the initial pick 'X' or 'O'
    show_board(positionboard, gameboard)

    game_on = True
    while game_on:
        for i in range(9):
            wincheck = check_win(gameboard)
            if wincheck:  # checking if winning condition is met
                print(f"\n\n\tCongratulations!\n\tPlayer {1 + int((i - 1) % 2 != 0)} wins!")
                game_on = False
                break
            else:
                movecheck = check_move(gameboard)
                if movecheck:
                    use_input(i, turns, positionboard, gameboard)
                else:
                    print('\n\n Match draw')
                    game_on = False
                    break
    if not replay():
        break
