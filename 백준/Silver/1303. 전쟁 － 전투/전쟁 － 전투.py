from collections import deque

N,M = map(int,input().split())
graph = [input() for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,s):
    count = 1
    q = deque()
    q.append((x,y))
    visited[y][x] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[ny][nx] == 0 and graph[ny][nx] == s:
                count +=1
                visited[ny][nx] = 1
                q.append((nx,ny))
    return count

total_W = 0
total_B = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] =="W":
            total_W += bfs(j,i,"W")**2
        elif visited[i][j] == 0 and graph[i][j] =="B":
            total_B += bfs(j, i,"B")**2

print(total_W,total_B)