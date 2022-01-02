def permute(nums: list[int]) -> list[list[int]]:
    def backtracking(perm):
        if len(perm) == len(nums):
            res.append(perm[::])
        else:
            for n in nums:
                if n not in set(perm):
                    perm.append(n)
                    backtracking(perm)
                    perm.pop()
    
    res = []
    perm = list()
    backtracking(perm)
    return res


if __name__ == '__main__':
    nums = [1,2,3]
    print(permute(nums))
