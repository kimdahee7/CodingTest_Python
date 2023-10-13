def solution(participant, completion):
    answer = ""
    l = {}
    for i in participant:
        if i in l:
            l[i] +=1
        else:
            l[i] = 1
    for j in completion:
        if j in l:
            l[j] -=1
    for k in l:
        if l[k] != 0:
            answer = k
    return answer