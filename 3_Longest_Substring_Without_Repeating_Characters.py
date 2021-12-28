def lengthOfLongestSubstring(s):
    char_to_pos = {}
    max_len = 0
    start = 0
    for i, c in enumerate(s):
        if c not in char_to_pos:
            char_to_pos[c] = i
        else:
            if char_to_pos[c] < start:
                char_to_pos[c] = i
            else:
                max_len = max(i-start, max_len)
                start = char_to_pos[c] + 1
                char_to_pos[c] = i
    max_len = max(len(s)-start, max_len)
    return max_len
if __name__ == '__main__':
    s = "abba"
    print(lengthOfLongestSubstring(s))

