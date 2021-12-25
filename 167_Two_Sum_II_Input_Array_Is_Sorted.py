def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            i += 1
if __name__ == '__main__':
    numbers = [2, 3, 4]
    target = 6
    print(twoSum(numbers, target))
