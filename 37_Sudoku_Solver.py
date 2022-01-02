def solveSudoku(board: list[list[str]]) -> None:
    def check(idx, num):
        i, j = all_empty_cells[idx]
        if board[i][j] ==  '.':
            if num not in row_to_nums[i] and \
               num not in col_to_nums[j] and \
               num not in subbox_to_nums[(i//3, j//3)]:
                return True
        return False

    def add(idx, num):
        i, j = all_empty_cells[idx]
        board[i][j] = num
        row_to_nums[i].add(num)
        col_to_nums[j].add(num)
        subbox_to_nums[(i//3, j//3)].add(num)


    def remove(idx, num):
        i, j = all_empty_cells[idx]
        board[i][j] = '.'
        row_to_nums[i].remove(num)
        col_to_nums[j].remove(num)
        subbox_to_nums[(i//3, j//3)].remove(num)

    def backtraking(idx, num):
        add(idx, num)
        if idx == len(all_empty_cells) - 1:
            return True
        else:
            for num in range(1, 10):
                num = str(num)
                if check(idx+1, num):
                    if backtraking(idx+1, num):
                        return True
                    else:
                        remove(idx+1, num)
            return False

    row_to_nums = {}
    col_to_nums = {}
    subbox_to_nums = {}
    all_empty_cells = []
    m = len(board)
    n = len(board[0])
    for i in range(m):
        if i not in row_to_nums:
            row_to_nums[i] = set()
        for j in range(n):
            if j not in col_to_nums:
                col_to_nums[j] = set()
            if (i//3, j//3) not in subbox_to_nums:
                subbox_to_nums[(i//3, j//3)] = set()
            if board[i][j] == '.':
                all_empty_cells.append([i, j])
            else:
                row_to_nums[i].add(board[i][j])
                col_to_nums[j].add(board[i][j])
                subbox_to_nums[(i//3, j//3)].add(board[i][j])
    idx = 0
    for num in range(1, 10):
        num = str(num)
        if check(idx, num):
            if backtraking(0, num):
                return board
            remove(idx, num)
    return board


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solveSudoku(board))
