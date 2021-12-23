def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i
if __name__ == '__main__':
    nums = [1,1,2]
    print(removeDuplicates(nums))
    print(nums)