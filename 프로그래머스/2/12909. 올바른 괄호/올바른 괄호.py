def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == ")" and len(stack) != 0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False