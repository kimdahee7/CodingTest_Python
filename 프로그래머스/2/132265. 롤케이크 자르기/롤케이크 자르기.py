from collections import Counter
def solution(topping):
    answer = 0
    total = len(set(topping))
    t = dict(Counter(topping))
    l = set()
    for i in topping:
        t[i] -=1
        l.add(i)
        if t[i] == 0:
            total-=1
        if total == len(l):
            answer +=1
    return answer