def solution(n):
    answer = 0
    stack = []
    i = 0
    while i <= n:
        if sum(stack) > n:
            stack.pop(0)
        elif sum(stack) == n:
            answer +=1
            stack.pop(0)
        else:
            i +=1
            stack.append(i)
    return answer