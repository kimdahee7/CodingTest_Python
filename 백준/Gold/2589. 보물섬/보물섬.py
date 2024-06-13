from collections import deque
N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
INF = 1e9

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    dist = [[INF for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((x, y))
    dist[y][x] = 0
    answer = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N and dist[ny][nx] > dist[b][a] + 1 and graph[ny][nx] == "L":
                dist[ny][nx] = dist[b][a] + 1
                q.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if dist[i][j] != INF:
                answer = max(answer,dist[i][j])
    return answer
a = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            a = max(a,bfs(j,i))
print(a)