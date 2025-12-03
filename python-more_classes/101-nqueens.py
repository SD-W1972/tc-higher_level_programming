#!/usr/bin/python3
"""
N-Queens Problem Solver
Solves the N queens puzzle (placing N non-attacking
queens on an N×N chessboard)
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed at board[row][col]
    """
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, board, row, solutions):
    """
    Backtracking function to find all solutions
    """
    if row == n:
        # Found a solution
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, board, row + 1, solutions)
            board[row] = -1  # Backtrack


def print_solutions(solutions):
    """
    Print all solutions in the required format
    """
    for solution in solutions:
        print(solution)


def main():
    # Validate arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Validate N >= 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve N-Queens problem
    board = [-1] * n  # Initialize board
    solutions = []
    solve_nqueens(n, board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
