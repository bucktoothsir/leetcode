def getRow(rowIndex):
    hash_table = {}
    def helper(i, j):
        if (i, j) in hash_table:
            return hash_table[(i, j)]
        if i == 0 or i == 1 or j == 0 or j == i:
            res = 1
        else:
            res = helper(i-1, j-1) + helper(i-1, j)
        hash_table[(i, j)] = res
        return res
    res = []
    for i in range(rowIndex+1):
        res.append(helper(rowIndex, i))
    return res

if __name__ == '__main__':
    rowIndex = 1
    print(getRow(rowIndex))
