def solution(s):
    answer = -1
    l = list(s)
    stack = [l[0]]
    for i in range(1,len(l)):
        if len(stack) == 0:
            stack.append(l[i])
        elif stack[-1] == l[i]:
            stack.pop()
        else:
            stack.append(l[i])
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer