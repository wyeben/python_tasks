def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")

    for _ in range(9):
        print_board(board)
        print(f"Player {player}, enter your move (row and column): ")

        while True:
            try:
                row, col = map(int, input().split())
                if board[row - 1][col - 1] == " ":
                    break
                else:
                    print("That cell is already taken. Try again: ")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column (e.g., 2 3): ")

        board[row - 1][col - 1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins! Congratulations!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
