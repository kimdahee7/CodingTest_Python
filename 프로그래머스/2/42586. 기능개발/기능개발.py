def solution(progresses, speeds):
    answer = []
    l = []
    for i in range(len(progresses)):
        k = (100-progresses[i]) // speeds[i]
        if (100-progresses[i]) % speeds[i] == 0:
            l.append(k)
        else:
            l.append(k+1)
    start = l[0]
    count = 1
    for i in range(1,len(l)):
        if l[i] <= start:
            count +=1
        else:
            answer.append(count)
            count = 1
            start = l[i]
    answer.append(count)
    return answer
