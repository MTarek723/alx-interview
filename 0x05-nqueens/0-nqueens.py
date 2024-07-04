#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage message and exit."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(msg):
    """Print error message and exit."""
    print(msg)
    sys.exit(1)


def is_valid(board, row, col):
    """
    Check if placing a queen at board[row] = col is valid.

    Args:
        board (list): The board.
        row (int): The current row.
        col (int): The current column.

    Returns:
        bool: True if valid, False otherwise.
    """
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(N, board, row):
    """
    Recursively solve the N queens problem and print each solution.

    Args:
        N (int): The size of the board.
        board (list): The board.
        row (int): The current row.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)
            board[row] = -1


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    board = [-1] * N
    solve_nqueens(N, board, 0)


if __name__ == "__main__":
    main()
