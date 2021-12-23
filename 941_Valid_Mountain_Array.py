def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i+1]:
        i += 1
    if i == 0 or i == len(arr) - 1:
        return False
    while i < len(arr) - 1 and arr[i] > arr[i+1]:
        i += 1
    if i == len(arr) - 1:
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [2,3,3,3]
    print(validMountainArray(nums))