def generate(numRows):
    res = []
    for i, n in enumerate(range(1, numRows+1)):
        res_n = [1] * n
        if i > 1:
            for j in range(1, n - 1):
                res_n[j] = res[i-1][j] + res[i-1][j-1]
        res.append(res_n)
    return res
if __name__ == '__main__':
    numRows = 1
    print(generate(numRows))


