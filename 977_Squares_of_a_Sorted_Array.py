def sortedSquares(nums):
    square_nums = [0] * len(nums)
    i = 0
    j = len(nums) - 1
    idx = len(nums) - 1

    while i <= j:
        if abs(nums[i]) >= abs(nums[j]):
            square_nums[idx] = nums[i]**2
            i += 1
        else:
            square_nums[idx] = nums[j]**2
            j -= 1
        idx -= 1
    return square_nums
    
if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    print(sortedSquares(nums))