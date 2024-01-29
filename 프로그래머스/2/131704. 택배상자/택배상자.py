def solution(order):
    answer = 0
    stack = []
    index = 0
    for i in range(1,len(order)+1):
        stack.append(i)
        while len(stack) > 0 and stack[-1] == order[index]:
            answer +=1
            index +=1
            stack.pop()
    return answer