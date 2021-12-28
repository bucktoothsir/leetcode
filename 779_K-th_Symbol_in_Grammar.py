def kthGrammar(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if n == 1:
        return 0
    else:
        last = kthGrammar(n-1, (k+1)//2)
        if k % 2 == 1:
            return last
        else:
            return (last + 1) % 2

if __name__ == '__main__':
    n = 2
    k = 2
    print(kthGrammar(n, k))
