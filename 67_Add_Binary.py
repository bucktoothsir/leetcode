def addBinary1(a, b):
    res = []
    i = len(a) - 1
    j = len(b) - 1
    addone = 0
    while i >= 0 and j >= 0:
        if a[i] == '1' and b[j] == '1':
            if addone:
                res.append('1')
            else:
                res.append('0')
            addone = 1
        elif a[i] == '1' or b[j] == '1':
            if addone:
                res.append('0')
            else:
                res.append('1')
        elif a[i] == '0' and b[j] == '0':
            if addone:
                res.append('1')
                addone = 0
            else:
                res.append('0')
        j -= 1
        i -= 1
    while i >= 0:
        if a[i] == '1':
            if addone:
                res.append('0')
            else:
                res.append('1')
        else:
            if addone:
                res.append('1')
                addone = 0
            else:
                res.append('0')
        i -= 1
    while j >= 0:
        if b[j] == '1':
            if addone:
                res.append('0')
            else:
                res.append('1')
        else:
            if addone:
                res.append('1')
                addone = 0
            else:
                res.append('0')
        j -= 1

    if addone:
        res.append('1')
    return ''.join(res[::-1])

def addBinary2(a, b):

if __name__ == '__main__':
    a = "100"
    b = "110010"
    print(addBinary1(a, b))



