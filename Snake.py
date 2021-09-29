def matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(input())
        matrix.append(row)

    return matrix



def snake_position(matrix):
    position = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            current_el = matrix[r][c]

            if current_el == 'S':
                position.append(r)
                position.append(c)

    return position

def position_is_B(matrix):
    b_position = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            current_el = matrix[r][c]
            if current_el == 'B':
                b_position.append(r)
                b_position.append(c)

    return b_position


def is_valid(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return True
    if col < 0 or col >= len(matrix):
        return True

    return False

current_matrix = matrix()
current_snake_position = snake_position(current_matrix)
row = current_snake_position[0]
col = current_snake_position[1]
food_eaten = 0
is_ok = False
while True:
    if food_eaten == 10:
        break

    direction = input()

    if direction == 'up':
        current_matrix[row][col] = '.'

        row = row - 1
        col = col
        if is_valid(current_matrix, row, col):
            is_ok = True
            break
        else:
            if current_matrix[row][col] == 'B':
                current_matrix[row][col] = '.'
                current_position = position_is_B(current_matrix, )
                row = current_position[0]
                col = current_position[1]

            if current_matrix[row][col] == '*':
                food_eaten += 1

            current_matrix[row][col] = 'S'

    elif direction == 'down':
        current_matrix[row][col] = '.'

        row = row + 1
        col = col
        if is_valid(current_matrix, row, col):
            is_ok = True
            break
        else:
            if current_matrix[row][col] == 'B':
                current_matrix[row][col] = '.'
                current_position = position_is_B(current_matrix)
                row = current_position[0]
                col = current_position[1]

            if current_matrix[row][col] == '*':
                food_eaten += 1

            current_matrix[row][col] = 'S'

    elif direction == 'left':
        current_matrix[row][col] = '.'

        row = row
        col = col - 1
        if is_valid(current_matrix, row, col):
            is_ok = True
            break
        else:
            if current_matrix[row][col] == 'B':
                current_matrix[row][col] = '.'
                current_position = position_is_B(current_matrix, )
                row = current_position[0]
                col = current_position[1]

            if current_matrix[row][col] == '*':
                food_eaten += 1

            current_matrix[row][col] = 'S'

    elif direction == 'right':
        current_matrix[row][col] = '.'

        row = row
        col = col + 1
        if is_valid(current_matrix, row, col):
            is_ok = True
            break
        else:
            if current_matrix[row][col] == 'B':
                current_matrix[row][col] = '.'
                current_position = position_is_B(current_matrix, )
                row = current_position[0]
                col = current_position[1]

            if current_matrix[row][col] == '*':
                food_eaten += 1

            current_matrix[row][col] = 'S'


if is_ok:
    print(f'Game over!')
    print(f'Food eaten: {food_eaten}')
    for n_row in range(len(current_matrix)):
        print(''.join(current_matrix[n_row]))
else:
    print(f'You won! You fed the snake.')
    print(f'Food eaten: {food_eaten}')
    for row_n in range(len(current_matrix)):
        print(''.join(current_matrix[row_n]))




# -----S
# ------
# ---B--
# ------
# -B----
# -*----