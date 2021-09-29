# I. Make a matrix with input
# II. Make the steps with a function
# III. When bomb explode check every direction and every diagonal for if it is bomb, if it is <= 0,
# IV. Make output
current_r = int(input())
current_c = current_r
def matrix_creator(r):
    matrix = []
    for _ in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix

current_matrix = matrix_creator(current_r)
def is_valid_bound(row, col):
    if 0 <= row < current_r and 0 <= col < current_r:
        return True
    return False

def bombs_counter(matrix, row, col):
    rows = [-1, -1, 0, 1, 1, 1, 0, -1]
    cols = [0, -1, -1, -1, 0, 1, 1, 1]
    all_stuff = []
    counter = 0
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]

        if is_valid_bound(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]

            all_stuff.append([])
            all_stuff[counter].append(potential_row)
            all_stuff[counter].append(potential_col)
            all_stuff[counter].append(potential_position)
            counter += 1

    return all_stuff



bomb_position = input().split()
for el in bomb_position:
    r, c = map(int, el.split(','))
    executed_nums = bombs_counter(current_matrix, r, c)
    for list_index in executed_nums:
        r_index = list_index[0]
        c_index = list_index[1]
        potential_position = list_index[2]

        if potential_position <= 0:
            pass
        if potential_position > 0:
            current_matrix[r_index][c_index] = current_matrix[r_index][c_index] - current_matrix[r][c]
    current_matrix[r][c] = 0

def answer2(matrix):
    for row in range(len(matrix)):
        current_row = [str(el) for el in matrix[row]]
        current_row = ' '.join(current_row)
        print(current_row)
      #  for col in range(len(matrix[row])):
       #     num = matrix[row][col]
        #    print(num, end=' ')

       # print()

def answer(matrix, r, c):
    alive_numbers = 0
    sum_of_alive_numbers = 0
    for r_num in range(r):
        for c_num in range(c):
            num = matrix[r_num][c_num]
            if num > 0:
                alive_numbers += 1
                sum_of_alive_numbers += num

    return alive_numbers, sum_of_alive_numbers

current_answer = answer(current_matrix, current_r, current_c)
print(f'Alive cells: {current_answer[0]}')
print(f'Sum: {current_answer[1]}')
answer2(current_matrix)



#3
# 7 8 4
# 3 1 5
# 6 4 9
# 0,2 1,0 2,2