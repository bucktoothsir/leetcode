def duplicateZeros(arr):
    num_of_zeros = 0
    last_zero_idx = -1
    for i, n in enumerate(arr):
        if i + num_of_zeros >= len(arr) - 1:
            break
        if n == 0:
            num_of_zeros += 1
            last_zero_idx = i

    i = len(arr) - num_of_zeros - 1
    j = len(arr) - 1
    while i >= 0:
        arr[j] = arr[i]
        if arr[i] == 0 and i <= last_zero_idx:
            j -= 1
            arr[j] = 0
        j -= 1
        i -= 1
    return arr

if __name__ == '__main__':
    arr = [0,1,7,6,0,2,0,7]
    print(duplicateZeros(arr))


        