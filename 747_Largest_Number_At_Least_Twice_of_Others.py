def dominantIndex1(nums):
    max_num = max(nums)
    idx = -1
    for i, n in enumerate(nums):
        if n != max_num:
            if n * 2 > max_num:
                return -1
        else:
            idx = i
    return idx

def dominantIndex2(nums):
    first_max = -1
    second_max = -1
    first_max_idx = -1
    for i, n in enumerate(nums):
        if n > first_max:
            first_max, second_max = n, first_max
            first_max_idx = i
        elif n < first_max and n > second_max:
            second_max = n
    if second_max * 2 <= first_max:
        return first_max_idx
    else:
        return -1


if __name__ == '__main__':
    nums = [3,6,1,0]
    print(dominantIndex1(nums))
    print(dominantIndex2(nums))
