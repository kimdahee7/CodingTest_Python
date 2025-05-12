from itertools import combinations

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

l = []
for i in range(N):
    for j in range(N):
        l.append((j,i)) #(x,y)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 1e9

combi = combinations(l,3)
for com in combi:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    total = 0
    cnt = 0
    for c in com:
        x,y = c
        total += graph[y][x]
        visited[y][x] = 1
        cnt +=1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == 0:
                total += graph[ny][nx]
                visited[ny][nx] = 1
                cnt +=1
    if cnt == 15:
        answer = min(answer,total)
print(answer)