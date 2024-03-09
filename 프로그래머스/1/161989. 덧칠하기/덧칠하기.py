def solution(n, m, section):
    answer = 1
    start = section[0]
    total = start + m -1
    for i in range(1,len(section)):
        if section[i] > total:
            start = section[i]
            total = start + m -1
            answer += 1
    return answer