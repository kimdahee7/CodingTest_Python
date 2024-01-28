def solution(ingredient):
    answer = 0
    l = []
    for i in ingredient:
        l.append(i)
        if len(l) >= 4 and l[len(l)-4:len(l)] == [1,2,3,1]:
            answer +=1
            l.pop()
            l.pop()
            l.pop()
            l.pop()
    return answer
        