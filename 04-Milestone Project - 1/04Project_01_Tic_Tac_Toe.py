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

##############################
# from IPython.display import clear_output# Global variables # to run in any IDE other than Jupyter notebook


def show_board(v_p, v_g):
    """
    DOCSTRING: Print two boards, One showing available positions, another one showing the game progress!
    :param v_p: board one, position list
    :param v_g: board two, game display list
    """
    # clear_output()    # to run in jupyter notebook
    print('\n' * 100)  # to run in any IDE other than Jupyter notebook

    # print the board
    print(" Available\t Game board\n positions\t  display!\n")
    print(f" {v_p['p7']} | {v_p['p8']} | {v_p['p9']} \t  {v_g['g7']} | {v_g['g8']} | {v_g['g9']}")
    print("-----------\t -----------")
    print(f" {v_p['p4']} | {v_p['p5']} | {v_p['p6']} \t  {v_g['g4']} | {v_g['g5']} | {v_g['g6']}")
    print("-----------\t -----------")
    print(f" {v_p['p1']} | {v_p['p2']} | {v_p['p3']} \t  {v_g['g1']} | {v_g['g2']} | {v_g['g3']}")


def initiate_game(preset):
    """
    DOCSTRING:  a list of 10 elements becomes a list of 9 elements (X and O in sequence according to player 1's choice)
    :param preset: a list, containing 10 moves ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    :return: a lis of 9 moves in sequence
    """
    p1symbol = input("\nPlayer 1, Pick X or O and press enter: ")
    if 'X' in p1symbol.upper():
        preset.pop(-1)
    elif 'O' in p1symbol.upper():
        preset.pop(0)
    else:
        # clear_output()    # to run in jupyter notebook
        print('\n' * 100)  # to run in any IDE other than Jupyter notebook
        print("\n\nWrong input!")
        initiate_game(preset)
    return preset


def use_input(loc, symbols, v_p, v_g):
    """
    DOCSTRING: asks for input position checks the input validity
    and shows the board after modifying the position list and game display list
    :param loc: an integer representing the turn number.
    :param symbols: a list containing 9 elements of X and O in sequence
    :param v_p: board one, position list
    :param v_g: board two, game display list
    """
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
    """
    DOCSTRING: checks all the winning conditions from game board display list
    :param vg: game board display list
    :return: Boolean
    """
    return (vg['g1'] == vg['g2'] == vg['g3'] != ' ') or (vg['g4'] == vg['g5'] == vg['g6'] != ' ') or (
            vg['g7'] == vg['g8'] == vg['g9'] != ' ') or (vg['g1'] == vg['g4'] == vg['g7'] != ' ') or (
                   vg['g2'] == vg['g5'] == vg['g8'] != ' ') or (vg['g3'] == vg['g6'] == vg['g9'] != ' ') or (
                   vg['g1'] == vg['g5'] == vg['g9'] != ' ') or (vg['g3'] == vg['g5'] == vg['g7'] != ' ')


def check_move(vg):
    """
    DOCSTRING: Checks for blank space in game board display list.
    :param vg: game board display list.
    :return: Boolean
    """
    return ' ' in vg.values()


def replay():
    """
    DOCSTRING: takes an input for yes or no and checks only the first letter is lower case y.
    :return: Boolean
    """
    return input('Play again? Enter Yes or No: ').lower().startswith('y')


while True:
    # clear_output()    # to run in jupyter notebook
    print('\n' * 100)   # to run in any IDE other than Jupyter notebook
    print("Welcome to Tic Tac Toe!")

    # Declare variables dictionaries representing two display board
    positionboard = {'p1': 1, 'p2': 2, 'p3': 3, 'p4': 4, 'p5': 5, 'p6': 6, 'p7': 7, 'p8': 8, 'p9': 9}
    gameboard = {'g1': ' ', 'g2': ' ', 'g3': ' ', 'g4': ' ', 'g5': ' ', 'g6': ' ', 'g7': ' ', 'g8': ' ', 'g9': ' '}
    # a set of 10 moves
    moveset = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']

    turns = initiate_game(moveset)          # all 9 moves in a sequence depending on the initial pick 'X' or 'O'
    show_board(positionboard, gameboard)    # Displays 2 boards

    game_on = True
    while game_on:
        for i in range(9):                          # max 9 moves
            wincheck = check_win(gameboard)         # checking if winning condition is met
            if wincheck:
                print(f"\n\n\tCongratulations!\n\tPlayer {1 + int((i - 1) % 2 != 0)} wins!")
                game_on = False
                break
            else:
                movecheck = check_move(gameboard)   # checking if moves available
                if movecheck:
                    use_input(i, turns, positionboard, gameboard)   # asking for input again
                else:
                    print('\n\n Match draw')
                    game_on = False
                    break
    if not replay():    # ask for replay the game
        break
