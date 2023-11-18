import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  graph[y][x] == 0
  while q:
    a,b = q.popleft()
    for i in range(8):
      ny = b + dy[i]
      nx = a + dx[i]
      if 0<=nx<w and 0<=ny<h and graph[ny][nx] == 1:
        q.append((nx,ny))
        graph[ny][nx] = 0
  
while True:
  graph = []
  total = 0
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  else:
    for i in range(h):
      m = list(map(int,input().split()))
      graph.append(m)
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        bfs(j,i)
        total +=1
  print(total)