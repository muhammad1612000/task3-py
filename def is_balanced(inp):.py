def is_balanced(inp):
    stack = []
    for c in inp:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if not stack:
                return "NO"
            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"


print(is_balanced("{()})("))
print(is_balanced("{[(]}"))
print(is_balanced("({})[]"))

