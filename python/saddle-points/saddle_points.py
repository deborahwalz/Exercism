def saddle_points(matrix):

    if matrix and len(set([len(row) for row in matrix])) != 1:
            raise ValueError("Invalid Matrix!")

    all_rows = [
        [[row_idx, i] for i, val in enumerate(row) if val >= max(row)] 
        for row_idx, row in enumerate(matrix)
    ]

    all_cols = [
        [[col_idx, i] for i, val in enumerate(col) if val <= min(col)]
        for col_idx, col in enumerate(zip(*matrix))
    ]

    for row in all_rows:
        for row_row, row_col in row:
            matrix[row_row][row_col] = "X"

    saddle_points = []

    for col in all_cols:
        for col_col, col_row in col:
            if matrix[col_row][col_col] == "X":
                saddle_points.append({"row": col_row + 1, "column": col_col + 1})

    return saddle_points