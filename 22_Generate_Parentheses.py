def generateParenthesis(n: int) -> list[str]:
    def backtracking(left, right, s):
        if left == n and right == n:
            res.append(s)
        if left <= n and left >= right:
            s += '('
            backtracking(left+1, right, s)
            s = s[:-1]
            s += ')'
            backtracking(left, right+1, s)
    res = []
    backtracking(0, 0, '')
    return res


if __name__ == '__main__':
    n = 1
    print(generateParenthesis(n))
