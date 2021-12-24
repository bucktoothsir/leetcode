def thirdMax(nums):
    if len(nums) < 3:
        return max(nums)
    i = 0
    first_max = -2**31 - 1
    second_max = -2**31- 1
    third_max = -2**31 - 1 
    for n in nums:
        if n > first_max:
            third_max = second_max
            second_max = first_max
            first_max = n
        elif n < first_max and n > second_max:
            third_max = second_max
            second_max = n
        elif n < second_max and n > third_max:
            third_max = n
    if third_max == -2**31 - 1:
        return first_max
    else:
        return third_max
if __name__ == '__main__':
    nums = [1,2,-2147483648]
    print(thirdMax(nums))



