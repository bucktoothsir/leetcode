def solveNQueens(n: int) -> list[list[str]]:
    def print_board(board):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q':
                    print('☆ '*j+'★ '+'☆ '*(n-j-1))
        print("\n\n")

    def create_board():
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            board.append(row)
        return board

    def check(row, col):
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n, 1)):
            if board[i][j] == 'Q':
                return False
        return True

    def backtracking(row):
        if row >= n:
            r = []
            for row in board:
                r.append(''.join(row))
            res.append(r)
        else:
            for i in range(n):
                if check(row, i):
                    board[row][i] = 'Q'
                    backtracking(row+1)
                    board[row][i] = '.'
                    

    if n > 0:
        board = create_board()
        res = []
        backtracking(0)
        for r in res:
            print_board(r)
        return res

if __name__ == '__main__':
    n = 1
    solveNQueens(n)


    