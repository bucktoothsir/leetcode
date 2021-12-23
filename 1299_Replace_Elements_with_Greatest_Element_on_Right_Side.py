def replaceElements(arr):
    if arr:
        max_num = arr[-1]
        arr[-1] = -1
        i = len(arr) - 2
        while i >= 0:
            if arr[i] > max_num:
                max_num, arr[i] = arr[i], max_num
            else:
                arr[i] = max_num
            i -= 1
    return arr
        
if __name__ == '__main__':
    arr = [400]
    replaceElements(arr)
    print(arr)
    

            

