def sortArray(nums):
    def merge(left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        return res

    if len(nums) <= 1:
        return nums
    else:
        left_sort = sortArray(nums[:len(nums)//2])
        right_sort = sortArray(nums[len(nums)//2:])
        return merge(left_sort, right_sort)

if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(sortArray(nums))
