def solution(N, stages):
    answer = []
    result = []
    for i in range(1,N+1):
        total = 0
        cnt = 0
        for j in stages:
            if i <= j:
                total +=1
                if i == j:
                    cnt +=1
        if cnt == 0 or total == 0:
            result.append((i,0))
        else:
            result.append((i,cnt/total))
    result.sort(key=lambda x:(-x[1],x[0]))
    for i in result:
        answer.append(i[0])
    return answer