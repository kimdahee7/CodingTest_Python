def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t)-length+1):
        window = t[i:i+length]
        if int(window) <= int(p):
            answer +=1
    return answer