from collections import deque

dx = [1,-1,0,0,1,-1,-1,1]
dy = [0,0,1,-1,1,-1,1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  graph[y][x] = 0
  while q:
    a,b = q.popleft()
    for i in range(8):
      ny = b + dy[i]
      nx = a + dx[i]
      if 0<=nx<N and 0<=ny<M and graph[ny][nx] == 1:
        q.append((nx,ny))
        graph[ny][nx] = 0
        

M,N = map(int,input().split())
graph = []
total = 0
for i in range(M):
  s = list(map(int,input().split()))
  graph.append(s)
for i in range(M):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(j,i)
      total +=1
print(total)