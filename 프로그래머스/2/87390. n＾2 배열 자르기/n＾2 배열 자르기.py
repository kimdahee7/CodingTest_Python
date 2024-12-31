def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        y = i//n + 1
        x = i%n + 1
        answer.append(max(y,x))
    return answer