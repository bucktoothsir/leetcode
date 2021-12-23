def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] & 1 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
if __name__ == '__main__':
    nums = [3,1,2,4]
    print(sortArrayByParity(nums))

    