def isValid(s):
    stack = list()
    for c in s:
        if c in '[({':
            stack.append(c)
        elif c == ']':
            if not len(stack) or stack.pop() != '[':
                return False
        elif c == '}':
            if not len(stack) or stack.pop() != '{':
                return False
        elif c == ')':
            if not len(stack) or stack.pop() != '(':
                return False
        else:
            return False
    if len(stack):
        return False
    else:
        return True
if __name__ == '__main__':
    s = "()"
    print(isValid(s))


