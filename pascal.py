print ""

import math

num_col = raw_input("How many rows should there be: ")

if num_col.isdigit():
	num_col = int(num_col)
	print ""
else:
	print "\nThat is not a number\n"
	quit()

def choose(col,pos):

    f = math.factorial

    global spot
    spot = f(col) / f(pos)
    spot = spot / f(col - pos)

triangle = []

for col in range(num_col):
    col_list = []
    for pos in range(col + 1):
        choose(col,pos)
        col_list.append(spot)

    triangle.append(col_list)

max_length = len(str(max(triangle[len(triangle) - 1])))

col_num = 0

for list in triangle:
    pos_num = 0
    for item in list:
        item = str(item)

        length = len(item)
        len_dif = max_length - length

        if len_dif % 2 == 0:
            num = len_dif / 2

            item = (" " * num) + item + (" " * num)

        else:
            num = len_dif / 2

            item = (" " * num) + item + (" " * num) + " "

        triangle[col_num][pos_num] = item
        pos_num += 1

    col_num += 1

col_num = 0
for j in triangle:
    column = ""
    for z in j:
        column += z + " "

    if num_col % 2 == 1:

        if col_num % 2 == 0:
            move_over = (num_col - col_num) / 2

            column = ((" " * max_length + " ") * move_over)+ column

        else:
            move_over = (num_col - col_num) / 2

            column = ((" " * max_length + " ") * (move_over - 1)) + (" " * ((max_length + 1) / 2)) + column

    else:

        if col_num % 2 == 1:
            move_over = (num_col - col_num) / 2

            column = ((" " * max_length + " ") * move_over)+ column

        else:
            move_over = (num_col - col_num) / 2

            column = ((" " * max_length + " ") * (move_over - 1)) + (" " * ((max_length + 1) / 2)) + column

    print column

    col_num += 1

print ""
