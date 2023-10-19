from itertools import combinations
def solution(k, tangerine):
    answer = 0
    box_dic = {}
    for i in tangerine:
        if i in box_dic:
            box_dic[i] +=1
        else:
            box_dic[i] = 1
    box_dic = sorted(box_dic.items(), key=lambda x:x[1],reverse=True)
    total = 0
    for i in box_dic:
        total += i[1]
        answer +=1
        if total >= k:
            return answer