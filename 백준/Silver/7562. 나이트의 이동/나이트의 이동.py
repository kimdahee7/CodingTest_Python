from collections import deque

dx = [2,1,-2,-1,2,1,-2,-1]
dy = [1,2,1,2,-1,-2,-1,-2]

def bfs(x1,y1,x2,y2,graph):
  q = deque()
  q.append((x1,y1))
  graph[y1][x1] = 0
  while q:
    a,b = q.popleft()
    if a == x2 and b == y2:
      print(graph[y2][x2])
      break
    for i in range(8):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<I and 0<=ny<I:
        if graph[ny][nx] > graph[b][a] + 1:
          graph[ny][nx] = graph[b][a] + 1
          q.append((nx,ny))

INF = 1e9

T = int(input())
for _ in range(T):
  I = int(input())
  a1,b1 = map(int,input().split())
  a2,b2 = map(int,input().split())
  graph = [[INF for _ in range(I)] for _ in range(I)]
  bfs(a1,b1,a2,b2,graph)