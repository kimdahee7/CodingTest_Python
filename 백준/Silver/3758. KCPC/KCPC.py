T = int(input())

for _ in range(T):
    n,k,t,m = map(int,input().split())
    dic = [[0 for _ in range(k+4)] for _ in range(n+1)]
    for index in range(n + 1):
        # 팀 id
        dic[index][0] = index
    for time in range(m):
        i,j,s = map(int,input().split())
        # 제출 횟수 카운트
        dic[i][k + 1] += 1
        # 마지막 제출 시간
        dic[i][k + 2] = time + 1
        if dic[i][j] < s:
            dic[i][j] = s
    for i in range(1,n+1):
        dic[i][k+3] = sum(dic[i][1:k+1])
    dic.sort(key=lambda x:(-x[k+3],x[k+1],x[k+2]))
    answer = 1
    for rank in range(n+1):
        if dic[rank][0] == t:
            print(answer)
            break
        else:
            answer +=1