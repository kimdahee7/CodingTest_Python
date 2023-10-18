def solution(s):
    answer = 0
    start = s[0]
    c = 0 
    nc = 0
    for i in range(len(s)):
        if s[i] == start:
            c +=1
            if c == nc:
                answer +=1
                c = 0
                nc = 0
                if i >= len(s)-1:
                    break
                else:
                    start = s[i+1]
        else:
            nc +=1
            if c == nc:
                answer +=1
                c = 0
                nc = 0
                if i >= len(s)-1: #10
                    break
                else:
                    start = s[i+1]
    if c != 0 or nc != 0:
        answer +=1
    return answer