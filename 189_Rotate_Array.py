def rotate(nums, k):
    length = len(nums)
    k %= length
    if k:
        i = 0
        next_idx = k + start
        end = next_idx
        last_num = nums[start]
        while i < length:
            last_num, nums[next_idx] = nums[next_idx], last_num
            i += 1
            next_idx = (next_idx + k) % length
            if next_idx == end:
                start += 1
                next_idx = (start + k) % length
                last_num = nums[start]
        return nums
if __name__ == '__main__':
    nums = [-1,-100,3,99]
    k = 2
    print(rotate(nums, k))

            
            

