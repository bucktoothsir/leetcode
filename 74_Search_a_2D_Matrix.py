def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    if m:
        n = len(matrix[0])
        if n:
            i = 0
            j = n - 1
            while i < m and j >= 0:
                if matrix[i][j] > target:
                    j -= 1
                elif matrix[i][j] < target:
                    i += 1
                else:
                    return True
    return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target))
