def arrayPairSum(nums):
    nums.sort()
    res = 0
    for i in range(0, len(nums), 2):
        res += nums[i]
    return res
if __name__ == '__main__':
    nums = [6,2,6,5,1,2]
    print(arrayPairSum(nums))

