from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

l = []

def bfs(x,y):
  c = 1
  q = deque()
  q.append((x,y))
  graph[y][x] = 0
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 1:
        q.append((nx,ny))
        c += 1
        graph[ny][nx] = 0
  l.append(c)

N,M,K = map(int,input().split())
graph = [[0 for _ in range(M)] for _ in range(N)] 
for i in range(K):
  x,y = map(int,input().split())
  graph[x-1][y-1] = 1

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      bfs(j,i)
print(max(l))