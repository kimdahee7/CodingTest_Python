from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dist = [[-1 for _ in range(m)]for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      dist[i][j] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  dist[y][x] = 0
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<m and 0<=ny<n and dist[ny][nx] == -1:
        dist[ny][nx] = dist[b][a] + 1
        q.append((nx,ny))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      bfs(j,i)
      break

for i in range(n):
  for j in range(m):
    print(dist[i][j], end= " ")
  print()
