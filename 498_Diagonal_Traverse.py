def findDiagonalOrder(mat):
    res = []
    i = 0
    j = 0
    m = len(mat)
    n = len(mat[0])
    while len(res) < m * n:
        while i >= 0 and j < n:
            res.append(mat[i][j])
            i -= 1
            j += 1
        if j < n:
            i += 1
        if j == n:
            i += 2
            j = n - 1
        while i < m and j >= 0:
            res.append(mat[i][j])
            i += 1
            j -= 1
        if i < m:
            j += 1
        if i == m:
            j += 2
            i = m - 1
    return res

if __name__ == '__main__':
    mat = [[1]]
    print(findDiagonalOrder(mat))
