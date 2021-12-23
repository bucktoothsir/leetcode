def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement(nums, val))
    print(nums)


