def countBinarySubstrings(s: str) -> int:
    res = 0
    start_a = 0
    start_b = 0
    i = 0
    while i < len(s):
        while i < len(s) and s[i] == s[start_a]:
            i += 1
        if i < len(s):
            start_b = i
        while i < len(s) and s[i] == s[start_b]:
            i += 1
        if i < len(s):
            res += min(start_b - start_a, i - start_b)
            start_a = start_b
            start_b = i
        
    res += min(start_b - start_a, i - start_b)
    return res
                
if __name__ == '__main__':
     s = "10101"
     print(countBinarySubstrings(s))
 