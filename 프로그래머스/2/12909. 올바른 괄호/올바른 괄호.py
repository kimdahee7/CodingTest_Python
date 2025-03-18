def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    return answer
