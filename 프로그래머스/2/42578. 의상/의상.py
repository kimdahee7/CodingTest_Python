def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] +=1
        else:
            dic[i[1]] = 1
    total = 1
    for a in dic.keys():
        total *= dic[a] + 1
    total -=1
    return total