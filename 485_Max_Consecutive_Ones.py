def max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for n in nums:
        if n == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    max_count = max(count, max_count)
    return max_count 

if __name__ == "__main__":
    nums = [1,0,1,1,0,1]
    print(max_consecutive_ones(nums))