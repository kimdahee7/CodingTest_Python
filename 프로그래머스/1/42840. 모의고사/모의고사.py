def solution(answers):
    answer = []
    l = len(answers)
    a = [1,2,3,4,5] * (l//5+1)
    b = [2,1,2,3,2,4,2,5] * (l//8+1)
    c = [3,3,1,1,2,2,4,4,5,5] * (l//10+1)
    a_c = 0
    b_c = 0
    c_c = 0
    for i in range(l):
        if a[i] == answers[i]:
            a_c +=1
        if b[i] == answers[i]:
            b_c +=1
        if c[i] == answers[i]:
            c_c +=1
    result = [a_c,b_c,c_c]
    max_data = max(result)
    for i in range(3):
        if result[i] == max_data:
            answer.append(i+1)
    return answer