def minRemoveToMakeValid(s):
    stack = list()
    idx_of_remove = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if not len(stack):
                idx_of_remove.append(i)
            else:
                stack.pop()
    res = ''
    for i, c in enumerate(s):
        if i not in idx_of_remove and i not in stack:
            res += c
    return res

if __name__ == '__main__':
    s =  "a)b(c)d"
    print(minRemoveToMakeValid(s))
        