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
    i = 0
    j = 0
    reverse_s = ''
    while j < len(s):
        while j < len(s) and s[j] != ' ':
            j += 1
        if j > i:
            reverse_s += reverseWord(s[i:j])
            reverse_s += ' '
        i = j + 1
        j = i
    return reverse_s[:-1]

if __name__ == '__main__':
    s = "God Ding"
    print(reverseWords(s))