def letterCombinations(digits: str) -> list[str]:
    def backtracking(s, i):
        if len(s) == len_of_digits:
            res.append(s)
        if i < len_of_digits:
            for c in digit_to_char[int(digits[i])]:
                s += c
                backtracking(s, i+1)
                s = s[:-1]
        
    digit_to_char = {2: 'abc',
                     3: 'def', 
                     4: 'ghi', 
                     5: 'jkl', 
                     6: 'mno', 
                     7: 'pqrs', 
                     8: 'tuv', 
                     9: 'wxyz', }
    len_of_digits = len(digits)
    res = []
    if len(digits):
        backtracking('', 0)
    return res

if __name__ == '__main__':
    digits = "2"
    print(letterCombinations(digits))


