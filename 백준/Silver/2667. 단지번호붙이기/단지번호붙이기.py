import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
result = []

def bfs(x,y):
  c = 1
  q = deque()
  q.append((x,y))
  graph[y][x] = 0
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N and graph[ny][nx] == 1:
        q.append((nx,ny))
        graph[ny][nx] = 0
        c +=1
  result.append(c)
total = 0
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(j,i)
      total +=1
print(total)
result.sort()
for i in result:
  print(i)