from collections import defaultdict

def solution(tickets):
    answer = []
    l = []
    dic = defaultdict(list)
    for i in tickets:
         dic[i[0]].append(i[1])
    for i in dic:
        dic[i].sort(reverse=True)
    
    l.append("ICN")
    while l:
        if l[-1] not in dic or len(dic[l[-1]]) == 0:
            answer.append(l.pop())
        else:
            l.append(dic[l[-1]].pop())
            
    return answer[::-1]