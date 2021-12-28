def reverseWord(w):
    w = list(w)
    i = 0
    j = len(w) - 1
    while i <= j:
        w[i], w[j] = w[j], w[i]
        i += 1
        j -= 1
    return ''.join(w)

def reverseWords(s):
    i = len(s) - 1
    j = len(s) - 1
    reverse_s = ''
    while j >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        if j < i:
            reverse_s += s[j+1:i+1]
            reverse_s += ' '
        i = j
    return reverse_s[:-1]

if __name__ == '__main__':
    s = "  hello world  "
    print(reverseWords(s))

    
