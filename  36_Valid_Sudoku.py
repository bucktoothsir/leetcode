def isValidSudoku(board: list[list[str]]) -> bool:
    row_to_nums = {}
    col_to_nums = {}
    subbox_to_nums = {}
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                continue
            if i not in row_to_nums:
                row_to_nums[i] = set()
            if board[i][j] in row_to_nums[i]:
                return False
            else:
                row_to_nums[i].add(board[i][j])
            if j not in col_to_nums:
                col_to_nums[j] = set()
            if board[i][j] in col_to_nums[j]:
                return False
            else:
                col_to_nums[j].add(board[i][j])
            if (i//3, j//3) not in subbox_to_nums:
                subbox_to_nums[(i//3, j//3)] = set()
            if board[i][j] in subbox_to_nums[(i//3, j//3)]:
                return False
            else:
                subbox_to_nums[(i//3, j//3)].add(board[i][j])
    return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))



