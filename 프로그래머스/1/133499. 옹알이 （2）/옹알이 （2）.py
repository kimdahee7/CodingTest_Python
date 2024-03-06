from itertools import product
def solution(babbling):
    answer = 0
    l = ["aya","ye","woo","ma"]
    exp = []
    new_l = []
    for i in l:
        exp.append(i*2)
    for i in babbling:
        c = 0
        for j in exp:
            if j in i:
                c +=1
                break
        if c == 0:
            for j in l:
                if j in i:
                    i = i.replace(j," ")
            if len(i.strip()) == 0:
                answer +=1
    return answer