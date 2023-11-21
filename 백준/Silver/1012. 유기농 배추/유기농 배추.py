from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[y][x] = 0
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<M and 0<=ny<N and visited[ny][nx] == 1:
        q.append((nx,ny))
        visited[ny][nx] = 0

T = int(input())
for _ in range(T):
  M,N,K = map(int,input().split())
  graph = [[] for i in range(N)]
  visited = [[0 for i in range(M)] for j in range(N)]
  for _ in range(K):
    a,b = map(int,input().split())
    graph[b].append(a)
    visited[b][a] = 1
    
  total = 0
  for i in range(N):
    for j in range(M):
      if visited[i][j] == 1:
        bfs(j,i)
        total +=1
  print(total)