def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid_move(grid, row, col, num):
    return (
        all(num != grid[row][i] for i in range(9)) and
        all(num != grid[i][col] for i in range(9)) and
        all(num != grid[row//3*3+i//3][col//3*3+i%3] for i in range(9))
    )

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True
    row, col = empty_location

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku puzzle:")
    print_grid(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku puzzle:")
        print_grid(puzzle)
    else:
        print("\nNo solution exists.")