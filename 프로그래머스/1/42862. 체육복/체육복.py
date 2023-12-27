def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort()
    reserve.sort()
    l = []
    for r in lost:
        if r in reserve:
            answer +=1
            reserve.remove(r)
            l.append(r)
    for i in l:
        lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer +=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer +=1
    return answer