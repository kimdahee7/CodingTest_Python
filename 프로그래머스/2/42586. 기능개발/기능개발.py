def solution(progresses, speeds):
    answer = []
    result = []
    day = 0
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            day = (100-progresses[i])//speeds[i]
            result.append(day)
        else:
            day = (100-progresses[i])//speeds[i] +1
            result.append(day)
    start = result[0]
    total = 0
    for i in result:
        if i <= start:
            total +=1
        else:
            answer.append(total)
            start = i
            total = 1
    answer.append(total)
    return answer