from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    l = []
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        total = 0
        l = discount[i:i+10]
        dic2 = dict(Counter(l))
        for k in range(len(want)):
            if want[k] not in l:
                break
            if dic[want[k]] != dic2[want[k]]:
                break
            total +=1
        if total == len(dic):
            answer +=1
    return answer