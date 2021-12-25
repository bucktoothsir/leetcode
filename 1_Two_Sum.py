from typing import no_type_check


def twoSum(nums, target):
    num_to_idx = {}
    for i, n in enumerate(nums):
        if target - n in num_to_idx:
            return [i, num_to_idx[target-n]]
        else:
            num_to_idx[n] = i

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(twoSum(nums, target))