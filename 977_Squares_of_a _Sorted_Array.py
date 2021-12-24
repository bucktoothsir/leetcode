def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    i = len()
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            squares.append(nums[left]**2)
            left += 1
        else:
            squares.append(nums[right]**2)
            right -= 1
    return squares[::-1]
if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))


