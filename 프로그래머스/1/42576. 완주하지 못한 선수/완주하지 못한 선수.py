from collections import Counter
def solution(participant, completion):
    answer = ''
    l = Counter(participant)
    for i in completion:
        if i in l:
            l[i] -=1
    for a in l:
        if l[a] == 1:
            answer = a
    return answer