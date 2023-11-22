from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph = []
graph1 = []
N = int(input())
for _ in range(N):
  l = list(input())
  graph.append(l)
graph1 = copy.deepcopy(graph)
  
def bfs(x,y,s,g):
  q = deque()
  q.append((x,y))
  g[y][x] = "0"
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<N and 0<=ny<N and g[ny][nx] == s:
        q.append((nx,ny))
        g[ny][nx] = "0"

total1 = 0
for i in range(N):
  for j in range(N):
    if graph[i][j] == "R" or graph[i][j] == "G" or graph[i][j] == "B":
      bfs(j,i,graph[i][j],graph)
      total1 +=1

for i in range(N):
  for j in range(N):
    if graph1[i][j] == "G":
      graph1[i][j] = "R"

total2 = 0
for i in range(N):
  for j in range(N):
    if graph1[i][j] == "R" or graph1[i][j] == "B":
      bfs(j,i,graph1[i][j],graph1)
      total2 +=1
print(total1, total2)