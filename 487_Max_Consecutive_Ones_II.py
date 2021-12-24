def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = 0
    one_zero = 0
    max_len = 0
    while right < len(nums):
        if not nums[right]:
            if one_zero:
                max_len = max(max_len, right-left)
                while nums[left]:
                        left += 1
                left += 1
            else:
                one_zero = 1
        right += 1
    max_len = max(max_len, right-left)
    return max_len

if __name__ == '__main__':
    nums = [0]
    print(findMaxConsecutiveOnes(nums))

                