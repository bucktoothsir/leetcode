def totalNQueens(n: int) -> int:

    def create_board():
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            board.append(row)
        return board

    def check(row: int, col: int) -> bool:
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 1:
                return False
        return True

    def backtracking(row: int):
        if row >= n:
            return 1
        num_of_sol = 0
        for i in range(n):
            if check(row, i):
                board[row][i] = 1
                num_of_sol += backtracking(row+1)
                board[row][i] = 0
        return num_of_sol
    board = create_board()
    num_of_sol = backtracking(0)
    return num_of_sol


if __name__ == '__main__':
    n = 4
    print(totalNQueens(n))