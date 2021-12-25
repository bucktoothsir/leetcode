def spiralOrder(matrix):
    res = []
    m = len(matrix)
    n = len(matrix[0])
    up = 0
    down = m - 1
    left = 0
    right = n - 1
    while len(res) < m * n:
        for i in range(left, right + 1):
            res.append(matrix[up][i])
        for i in range(up + 1, down + 1):
            res.append(matrix[i][right])
        if up != down:
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[down][i])
        if left != right:
            for i in range(down - 1, up, -1):
                res.append(matrix[i][left])
        up += 1
        left += 1
        right -= 1
        down -= 1
    return res

if __name__ == '__main__':
    matrix = [[7],[9],[6]]
    print(spiralOrder(matrix))
    7
    9
    6
            
        