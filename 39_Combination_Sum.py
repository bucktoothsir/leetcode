def combinationSum(candidates: list[int], target: int) -> list[list[int]]:

    def backtracking(comb, remain, start):
        if remain == 0:
            res.append(comb[::])
        elif remain > 0:
            i = start
            while i < len(candidates):
                num = candidates[i]
                if num <= remain:
                    comb.append(num)
                    remain -= num
                    backtracking(comb, remain, i)
                    remain += num
                    comb.pop()
                    i += 1
                else:
                    break
    
    res = []
    i = 0
    while i < len(candidates):
        num = candidates[i]
        comb = []
        comb.append(num)
        remain = target - num
        backtracking(comb, remain, i)
        comb.pop()
        i += 1
    return res
                

if __name__ == '__main__':
    candidates = [2,7,6,3,5,1]
    target = 4
    print(combinationSum(candidates, target))

