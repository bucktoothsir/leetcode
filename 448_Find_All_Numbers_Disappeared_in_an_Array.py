def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        j = nums[i] - 1
        while nums[i] != i + 1 and nums[j] != j + 1:
            nums[i], nums[j] = nums[j], nums[i]
            j = nums[i] - 1
    res = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i+1)
    return res
if __name__ == '__main__':
    nums = [1,1]
    print(findDisappearedNumbers(nums))
