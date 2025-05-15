import random

def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check cols
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def player_move(board):
    while True:
        try:
            move = input("Masukkan posisi (1-9) tempat Anda ingin menaruh 'X': ")
            pos = int(move) - 1
            if pos < 0 or pos > 8:
                print("Posisi tidak valid. Masukkan angka antara 1 sampai 9.")
                continue
            row, col = divmod(pos, 3)
            if board[row][col] != " ":
                print("Posisi sudah terisi, pilih posisi lain.")
                continue
            board[row][col] = "X"
            break
        except ValueError:
            print("Input tidak valid, masukkan angka antara 1 sampai 9.")

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    elif check_winner(board, "X"):
        return depth - 10
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (i,j) in get_available_moves(board):
            board[i][j] = "O"
            score = minimax(board, depth+1, False)
            board[i][j] = " "
            if score > best_score:
                best_score = score
        return best_score
    else:
        best_score = float('inf')
        for (i,j) in get_available_moves(board):
            board[i][j] = "X"
            score = minimax(board, depth+1, True)
            board[i][j] = " "
            if score < best_score:
                best_score = score
        return best_score

def computer_move_easy(board):
    moves = get_available_moves(board)
    move = random.choice(moves)
    board[move[0]][move[1]] = "O"

def computer_move_hard(board):
    best_score = -float('inf')
    best_move = None
    for (i,j) in get_available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i,j)
    if best_move:
        board[best_move[0]][best_move[1]] = "O"

def main():
    print("Selamat datang di Tic Tac Toe melawan Komputer!")
    print("Anda bermain dengan 'X', komputer dengan 'O'.")
    print("Masukkan posisi papan sebagai angka 1 sampai 9 seperti berikut:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

    while True:
        difficulty = input("Pilih tingkat kesulitan komputer (mudah/sulit): ").lower()
        if difficulty in ['mudah', 'sulit']:
            break
        else:
            print("Pilihan tidak valid, ketik 'mudah' atau 'sulit'.")

    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        player_move(board)
        if check_winner(board, "X"):
            print_board(board)
            print("Selamat! Anda menang!")
            break
        if check_draw(board):
            print_board(board)
            print("Permainan seri!")
            break

        print("Giliran komputer...")
        if difficulty == "mudah":
            computer_move_easy(board)
        else:
            computer_move_hard(board)

        if check_winner(board, "O"):
            print_board(board)
            print("Maaf, komputer menang!")
            break
        if check_draw(board):
            print_board(board)
            print("Permainan seri!")
            break

    print("Terima kasih sudah bermain!")

if __name__ == "__main__":
    main()