from collections import deque
N,M = map(int,input().split())
INF = 1e9
graph = [list(map(str,input())) for _ in range(N)]
dist = [[INF for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
q.append((0,0))
dist[0][0] = 1
while q:
    a,b = q.popleft()
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[ny][nx] == "1":
            if dist[ny][nx] > dist[b][a] +1:
                dist[ny][nx] = dist[b][a] +1
                q.append((nx,ny))
print(dist[N-1][M-1])