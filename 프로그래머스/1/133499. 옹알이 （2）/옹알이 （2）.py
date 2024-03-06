from itertools import product
def solution(babbling):
    l = ["aya","ye","woo","ma"]
    exp = []
    new_l = []
    for i in l:
        exp.append(i*2)
    for i in babbling:
        c = 0 
        for j in exp:
            if j in i:
                c += 1
                break
        if c  == 0:
            new_l.append(i)
    answer = len(new_l)
    for i in new_l:
        for j in l:
            if j in i:
                i = i.replace(j,"0")
        for a in i:
            if a != "0":
                answer -=1
                break
    return answer