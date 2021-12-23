def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
if __name__ == '__main__':
    nums = [1,0,1,0]
    moveZeroes(nums)
    print(nums)