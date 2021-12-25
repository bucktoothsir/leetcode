def pivotIndex1(nums):
    sum_from_left = [0]
    left_sum = 0
    for n in nums:
        left_sum += n
        sum_from_left.append(left_sum)
    
    sum_from_right = [0]
    right_sum = 0
    for n in nums[::-1]:
        right_sum += n
        sum_from_right.append(right_sum)
    
    for i in range(len(nums)):
        if sum_from_left[i] == sum_from_right[len(nums)-i-1]:
            return i
    return -1

def pivotIndex2(nums):
    sum_of_nums = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        sum_of_nums -= nums[i]
        if left_sum == sum_of_nums:
            return i
        left_sum += nums[i]
    return -1

if __name__ == '__main__':
    nums =  [2,1,-1]
    print(pivotIndex1(nums))
    print(pivotIndex2(nums))
