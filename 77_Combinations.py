def combine(n: int, k: int) -> list[list[int]]:
    def check(comb, num):
        if num in set(comb):
            return False
        else:
            return True

    def backtraking(comb, num, start):
        comb.append(num)
        if len(comb) == k:
            res.append(comb[::])
        else:
            for num in range(start, n+1):
                if check(comb, num):
                    backtraking(comb, num, num+1)
                    comb.pop()
    res = []
    for num in range(1, n+1):
        comb = []
        if check(comb, num):
            backtraking(comb, num, num+1) 
    return res

if __name__ == '__main__':
    n = 5
    k = 3
    print(combine(n, k))
