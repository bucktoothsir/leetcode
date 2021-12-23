def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    set_of_arr = set()
    for n in arr:
        if (n % 2 == 0 and n // 2 in set_of_arr) or n * 2 in set_of_arr:
            return True
        set_of_arr.add(n)
    return False
if __name__ == '__main__':
    nums = [-2,0,10,-19,4,6,-8]
    print(checkIfExist(nums))

    