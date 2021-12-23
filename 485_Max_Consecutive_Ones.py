def max_consecutive_ones(nums):
    max_len_of_con_ones = 0
    start = -1
    end = -1
    for i in range(len(nums)):
        if nums[i] == 1:
            if end < i or start == -1:
                start = i
            end = i + 1
        else:
            if i > 0 and nums[i-1] == 1:
                 max_len_of_con_ones = max(max_len_of_con_ones, end-start)
        max_len_of_con_ones = max(max_len_of_con_ones, end-start)
    return max_len_of_con_ones

if __name__ == "__main__":
    nums = [1]
    print(max_consecutive_ones(nums))