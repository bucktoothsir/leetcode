def plusOne(digits):
    results = []
    addone = 1
    for d in digits[::-1]:
        d = d + addone
        addone = d // 10
        results.append(d % 10)
    if addone:
        results.append(1)
    return results[::-1]
if __name__ == '__main__':
    digits = [9]
    print(plusOne(digits))

