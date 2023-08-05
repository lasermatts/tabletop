#!/usr/bin/python
##a funky puzzle generator for all you netrunners 

##IMPORTS
import numpy as np
import math
import random

def is_valid(grid, row, col, num, size):
    box_size = int(math.sqrt(size))
    # Check if the number is already in the row or column
    for x in range(size):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check if the number is in the current box
    startRow = row - row % box_size
    startCol = col - col % box_size
    for i in range(box_size):
        for j in range(box_size):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solve_sudoku(grid, size, row=0, col=0):
    if row == (size - 1) and col == size:
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, size, row, col + 1)
    for num in range(1, size + 1):
        if is_valid(grid, row, col, num, size):
            grid[row][col] = num
            if solve_sudoku(grid, size, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def print_grid(grid, size):
    for i in range(size):
        for j in range(size):
            if isinstance(grid[i][j], str):  # print 'x' for removed numbers
                print(grid[i][j], end = " ")
            else:
                print(grid[i][j], end = " ")
        print()

def remove_numbers(grid, size, num_to_remove):
    while num_to_remove > 0:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if grid[row][col] != 0:
            grid[row][col] = 'x'  # replace removed numbers with 'x'
            num_to_remove -= 1
    return grid

def generate_sudoku(size, difficulty):
    # Create a list to store the Sudoku grid
    grid = [[0 for _ in range(size)] for _ in range(size)]
    # Generate a solved Sudoku
    nums = list(range(1, size + 1))
    for i in range(size):
        for j in range(size):
            np.random.shuffle(nums)
            grid[i][j] = nums[j]
    if solve_sudoku(grid, size):
        grid = remove_numbers(grid, size, difficulty)
        print_grid(grid, size)
    else:
        print("No solution exists")

def main():
    while True:
        difficulty = input("Please enter the difficulty (easy, medium, hard) or 'quit' to exit: ")
        if difficulty == "easy":
            generate_sudoku(4, 4)  # Removing 4 numbers for easy 4x4 Sudoku
        elif difficulty == "medium":
            generate_sudoku(6, 12)  # Removing 12 numbers for medium 6x6 Sudoku
        elif difficulty == "hard":
            generate_sudoku(9, 20)  # Removing 20 numbers for hard 9x9 Sudoku
        elif difficulty.lower() == "quit":
            break
        else:
            print("Invalid input. Please enter either 'easy', 'medium', 'hard', or 'quit'.")

if __name__ == "__main__":
    main()
