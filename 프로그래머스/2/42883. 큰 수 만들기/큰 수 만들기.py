def solution(number, k):
    n_l = list(map(int,number))
    stack = []
    count = 0
    for i in n_l:
        stack.append(i)
        while len(stack) >= 2 and stack[-2] < stack[-1] and count != k:
            stack.pop(-2)
            count +=1 
    while count != k:
        stack.pop()
        count +=1
    stack = map(str,stack)
    answer = ''.join(stack)
    return answer