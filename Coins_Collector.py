import math
def matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = (input().split())
        matrix.append(row)

    return matrix


def is_valid(matrix, row, col, coins):
    is_out = False
    if row < 0 or row >= len(matrix):
        coins = math.floor(coins - (coins * 0.5))
        is_out = True
        return coins, is_out
    if col < 0 or col >= len(matrix):
        coins = math.floor(coins - (coins * 0.5))
        is_out = True
        return coins, is_out


    return coins, is_out

def hits_wall(matrix, row, col, coins):
    current_move = matrix[row][col]
    is_hited = False
    if current_move == 'X':
        coins = math.floor(coins - (coins * 0.5))
        is_hited = True
        return coins, is_hited
    return coins, is_hited



def player_position(matrix):
    position = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            current_el = matrix[r][c]

            if current_el == 'P':
                position.append(r)
                position.append(c)

    return position


current_matrix = matrix()
n_coins = 0
current_player_position = player_position(current_matrix)
row = current_player_position[0]
col = current_player_position[1]
player_path = []
is_ok = False

while True:
    collect_coins = 0
    if n_coins >= 100:
        break

    direction = input()

    if direction == 'up':
        current_path = []

        row = row - 1
        col = col
        current_valid = is_valid(current_matrix, row, col, n_coins)
        if current_valid[1]:
            n_coins = current_valid[0]
            is_ok = True
            break
        current_hits_wall = hits_wall(current_matrix, row, col, n_coins)
        if current_hits_wall[1]:
            n_coins = current_hits_wall[0]
            is_ok = True
            break

        else:
            collect_coins = int(current_matrix[row][col])
            current_path.append(row)
            current_path.append(col)
            player_path.append(current_path)

            n_coins += collect_coins
            current_matrix[row][col] = 'P'

    elif direction == 'down':
        current_path = []

        row = row + 1
        col = col
        current_valid = is_valid(current_matrix, row, col, n_coins)
        if current_valid[1]:
            n_coins = current_valid[0]
            is_ok = True
            break
        current_hits_wall = hits_wall(current_matrix, row, col, n_coins)
        if current_hits_wall[1]:
            n_coins = current_hits_wall[0]
            is_ok = True
            break
        else:

            collect_coins = int(current_matrix[row][col])
            current_path.append(row)
            current_path.append(col)
            player_path.append(current_path)

            n_coins += collect_coins
            current_matrix[row][col] = 'P'

    elif direction == 'left':
        current_path = []

        row = row
        col = col - 1
        current_valid = is_valid(current_matrix, row, col, n_coins)
        if current_valid[1]:
            n_coins = current_valid[0]
            is_ok = True
            break
        current_hits_wall = hits_wall(current_matrix, row, col, n_coins)
        if current_hits_wall[1]:
            n_coins = current_hits_wall[0]
            is_ok = True
            break
        else:
            collect_coins = int(current_matrix[row][col])
            current_path.append(row)
            current_path.append(col)
            player_path.append(current_path)

            n_coins += collect_coins
            current_matrix[row][col] = 'P'

    elif direction == 'right':
        current_path = []

        row = row
        col = col + 1
        current_valid = is_valid(current_matrix, row, col, n_coins)
        if current_valid[1]:
            n_coins = current_valid[0]
            is_ok = True
            break
        current_hits_wall = hits_wall(current_matrix, row, col, n_coins)
        if current_hits_wall[1]:
            n_coins = current_hits_wall[0]
            is_ok = True
            break
        else:
            collect_coins = int(current_matrix[row][col])
            current_path.append(row)
            current_path.append(col)
            player_path.append(current_path)

            n_coins += collect_coins
            current_matrix[row][col] = 'P'
    else:
        pass

if is_ok:
    print(f"Game over! You've collected {n_coins} coins.")
    print(f'Your path:')
    for n_row in player_path:
        print(n_row)
else:
    print(f"You won! You've collected {n_coins} coins.")
    print(f'Your path:')
    for n_row in player_path:
        print(n_row)


# 5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# right
# right
# up
# up
# left
# down



# 8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# left