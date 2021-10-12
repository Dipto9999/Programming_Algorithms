def mine_sweeper(bombs, num_rows, num_cols) :
    field = [[0 for j in range(num_cols)] for i in range(num_rows)]

    for bomb_location in bombs :
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range : 
            current_row = i

            for j in col_range :
                current_col = j

                if (0 <= current_row <= num_rows and 0 <= current_col <= num_cols and field[i][j] != -1) :
                    field[i][j] += 1

    return field

print (mine_sweeper([[0,0], [1,2]], 3, 4))    