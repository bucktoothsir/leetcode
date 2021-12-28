def myPow(x, n):
    hash_table = {}
    def helper(x, n):
        if n in hash_table:
            return hash_table[n]
        else:
            if n == 1:
                res = x
            elif n % 2:
                res = helper(x, n//2) ** 2 * x
            else:
                res = helper(x, n//2) ** 2
            hash_table[n] = res
            return res
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n 
    return helper(x, n)

if __name__ == '__main__':
    x = 2.10000
    n = 3
    print(myPow(x, n))

