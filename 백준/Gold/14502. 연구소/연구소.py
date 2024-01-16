from collections import deque
from itertools import combinations
import copy
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
l = []
c_l = []
s_l = []
result = []

copy_graph = copy.deepcopy(graph)

for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      l.append((j,i))

for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      s_l.append((j,i))

c_l = list(combinations(l,3))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph):
  q = deque()
  for i in s_l:
    x1 = i[0]
    y1 = i[1]
    q.append((x1,y1))
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 0:
        graph[ny][nx] = 2
        q.append((nx,ny))
  total = 0
  for x in range(N):
    for y in range(M):
      if graph[x][y] == 0:
        total +=1
  result.append(total)

for i in c_l:
  for j in i:
    graph[j[1]][j[0]] = 1
  bfs(graph)
  graph = copy.deepcopy(copy_graph)

print(max(result))
