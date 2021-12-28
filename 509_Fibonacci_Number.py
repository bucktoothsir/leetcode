def fib(n):
    hash_table = {}
    def helper(n):
        if n in hash_table:
            return hash_table[n]
        else:
            if n == 0 or n == 1:
                result = n
            else:
                result = helper(n-1) + helper(n-2)
            hash_table[n] = result
            return result
    res =  helper(n)
    return res

if __name__ == '__main__':
    n = 4
    print(fib(n))

    