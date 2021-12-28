import string
def originalDigits(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine']
    char_to_freq = dict(zip(string.ascii_lowercase, [0]*26))
    for c in s:
        char_to_freq[c] += 1
    num_to_freq = dict(zip(range(10), [0]*10))
    num_to_freq[0] = char_to_freq['z']
    num_to_freq[2] = char_to_freq['w']
    num_to_freq[6] = char_to_freq['x']
    num_to_freq[8] = char_to_freq['g']
    num_to_freq[7] = char_to_freq['s'] - num_to_freq[6]
    num_to_freq[5] = char_to_freq['v'] - num_to_freq[7]
    num_to_freq[3] = char_to_freq['h'] - num_to_freq[8]
    num_to_freq[9] = char_to_freq['i'] - num_to_freq[5] - num_to_freq[6] - num_to_freq[8]
    num_to_freq[4] = char_to_freq['f'] - num_to_freq[5]
    num_to_freq[1] = char_to_freq['o'] - num_to_freq[0] - num_to_freq[2] - num_to_freq[4]
    res = ''
    for i in range(10):
        if num_to_freq[i]:
            res += num_to_freq[i] * str(i)
    return res

if __name__ == '__main__':
    s = "owoztneoer"
    print(originalDigits(s))
