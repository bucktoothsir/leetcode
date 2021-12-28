def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    def help(up: int, down: int, left: int, right: int, target: int)  -> bool:
        if up > down or left > right:
            return False
        i = (up + down) // 2
        j = (left + right) // 2
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            return help(up, i-1, left, right, target) or \
                   help(i, down, left, j-1, target)
        else:
            return help(up, down, j+1, right, target) or \
                    help(i+1, down, left, j, target)
    up = 0
    down = len(matrix) - 1
    if down >= 0:
        left = 0
        right = len(matrix[0]) - 1
        return help(up, down, left, right, target)
    return False

if __name__ == '__main__':
    matrix = [[-5]]
    target = -5
    print(searchMatrix(matrix, target))
