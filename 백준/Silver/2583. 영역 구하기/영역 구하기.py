import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

M,N,K = map(int,input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]    
for i in range(K):
  x1,y1,x2,y2 = map(int,input().split())
  for i in  range(min(y1,y2),max(y1,y2)):
    for j in range(min(x1,x2),max(x1,x2)):
      graph[i][j] = 1
      
result = []
def bfs(x,y):
  c = 1
  q = deque()
  q.append((x,y))
  graph[y][x] = 1
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M and graph[ny][nx] == 0:
        q.append((nx,ny))
        graph[ny][nx] = 1
        c += 1
  result.append(c)
  
total = 0
for i in range(M):
  for j in range(N):
    if graph[i][j] == 0:
      bfs(j,i)
      total +=1
print(total)
result.sort()
for i in result:
  print(i,end=" ")