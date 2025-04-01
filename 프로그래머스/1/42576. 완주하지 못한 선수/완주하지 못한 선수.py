def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] +=1
    for c in completion:
        dic[c] -=1
    for i in dic:
        if dic[i] != 0 :
            answer = i
    return answer