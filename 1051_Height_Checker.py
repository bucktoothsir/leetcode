def heightChecker(heights):
    height_to_freq = {}
    for h in heights:
        if h not in height_to_freq:
            height_to_freq[h] = 1
        else:
            height_to_freq[h] += 1
    h_ptr = 1
    res = 0
    for h in heights:
        while height_to_freq[h] == 0:
            h += 1
        if h_ptr != h:
            res += 1
        height_to_freq[h_ptr] -= 1
    return res

if __name__ == '__main__':
    heights = [5,1,2,3,4]
    print(heightChecker(heights))


    