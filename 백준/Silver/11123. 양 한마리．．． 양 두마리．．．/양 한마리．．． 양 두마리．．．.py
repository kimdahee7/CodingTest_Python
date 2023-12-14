from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  graph[y][x] = "."
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<W and 0<=ny<H and graph[ny][nx] == "#":
        q.append((nx,ny))
        graph[ny][nx] = "."

T = int(input())
for _ in range(T):
  total = 0
  H,W = map(int,input().split())
  graph = [list(input()) for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if graph[i][j] == "#":
        bfs(j,i)
        total +=1 
  print(total)