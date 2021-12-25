def minSubArrayLen(target, nums):
    i = -1
    j = 0
    sum_of_num = 0
    min_len = len(nums) + 1
    while j < len(nums):
        sum_of_num += nums[j]
        if sum_of_num >= target:
            while i <= j and sum_of_num >= target:
                i += 1
                sum_of_num -= nums[i]
            min_len = min(min_len, j - i + 1)
        j += 1
    if min_len == len(nums) + 1:
        return 0
    else:
        return min_len
if __name__ == '__main__':
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    target = 213
    print(minSubArrayLen(target, nums))

        
        