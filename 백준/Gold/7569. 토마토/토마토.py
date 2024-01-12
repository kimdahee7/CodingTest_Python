from collections import deque

M,N,H = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
INF = 1e9
dist = [[[INF] * M for _ in range(N)] for _ in range(H)]

dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]

q = deque()

def bfs():
  while q:
    a,b,c = q.popleft()
    for i in range(6):
      nx = a + dx[i]
      ny = b + dy[i]
      nz = c + dz[i]
      if 0<=nx<M and 0<=ny<N and 0<=nz<H and graph[nz][ny][nx] == 0:
        dist[nz][ny][nx] = dist[c][b][a] +1
        q.append((nx,ny,nz))
        graph[nz][ny][nx] = 1

for h in range(H):
  for n in range(N):
    for m in range(M):
      if graph[h][n][m] == 1:
        q.append((m,n,h))
        dist[h][n][m] = 0
      if graph[h][n][m] == -1:
        dist[h][n][m] = -1

bfs()

answer = 0
for h in range(H):
  for n in range(N):
    for m in range(M):
      answer = max(answer,dist[h][n][m])
if answer == INF:
  print(-1)
else:
  print(answer)