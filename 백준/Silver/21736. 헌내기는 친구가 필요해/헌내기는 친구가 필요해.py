from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x,y):
  total = 0
  q = deque()
  q.append((x,y))
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<M and 0<=ny<N and graph[ny][nx] != "X":
        if graph[ny][nx] == "P":
          total +=1
        q.append((nx,ny))
        graph[ny][nx] = "X"
  if total == 0:
    print("TT")
  else:
    print(total)


N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

for i in range(N):
  for j in range(M):
    if graph[i][j] == "I":
      bfs(j,i)