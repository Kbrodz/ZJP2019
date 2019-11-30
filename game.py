# Tic Tac Toe game in python

board = [' ' for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == ' '


def print_board(place):
    print(' ' + place[7] + ' | ' + place[8] + ' |  ' + place[9])
    print('-----------')
    print(' ' + place[4] + ' | ' + place[5] + ' |  ' + place[6])
    print('-----------')
    print(' ' + place[1] + ' | ' + place[2] + ' |  ' + place[3])


def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) \
        or (bo[4] == le and bo[5] == le and bo[6] == le) \
        or (bo[1] == le and bo[2] == le and bo[3] == le) \
        or (bo[1] == le and bo[4] == le and bo[7] == le)\
        or (bo[2] == le and bo[5] == le and bo[8] == le) \
        or (bo[3] == le and bo[6] == le and bo[9] == le) \
        or (bo[1] == le and bo[5] == le and bo[9] == le) \
        or (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        try:
            move = int(move)
            if number:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(table):
    if table.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to Tic Tac Toe!')
    print_board(board)

    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
            else:
                insert_letter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                print_board(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if is_board_full(board):
        print('Tie Game!')


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        print('-----------------------------------')
        main()
    else:
        break
