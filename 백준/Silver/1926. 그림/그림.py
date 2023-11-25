from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = []

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
      if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 1:
        q.append((nx,ny))
        graph[ny][nx] = 0
        c+=1
  result.append(c)
        

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]

total = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      bfs(j,i)
      total +=1
print(total)
if total == 0:
  print(0)
else:
  print(max(result))