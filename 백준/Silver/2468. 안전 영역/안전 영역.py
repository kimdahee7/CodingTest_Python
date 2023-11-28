import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,m):
  q = deque()
  q.append((x,y))
  visited[y][x] = True
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<N and 0<=ny<N and graph[ny][nx] >m and visited[ny][nx] == False:
        q.append((nx,ny))
        visited[ny][nx] = True
  

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
result = []
max_v = max(map(max, graph))
for i in range(max_v+1):
  total = 0 
  visited = [[False] * N for _ in range(N)]
  for y in range(N):
    for x in range(N):
      if graph[y][x] > i and visited[y][x] == False:
        bfs(x,y,i)
        total +=1
  result.append(total)
print(max(result))
  