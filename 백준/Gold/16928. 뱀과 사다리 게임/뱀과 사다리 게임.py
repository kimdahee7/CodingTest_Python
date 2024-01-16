from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(101)]
for _ in range(N):
  x,y = map(int,input().split())
  graph[x].append(y)
for _ in range(M):
  u,v = map(int,input().split())
  graph[u].append(v)
INF = 1e9
dist = [INF] * (101)
visited = [False] * (101)

dx = [1,2,3,4,5,6]

q = deque()
q.append(1)
dist[1] = 0
visited[1] = True
while q:
  x = q.popleft()
  for i in range(6):
    nx = x + dx[i]
    if 0<nx<=100 and visited[nx] == False:
      visited[nx] = True
      if len(graph[nx]) == 0:
        dist[nx] =dist[x]+1
        q.append(nx)
      else:
        if visited[graph[nx][0]] == False:
          dist[graph[nx][0]] = dist[x]+1
          q.append(graph[nx][0])
          visited[graph[nx][0]] = True
print(dist[100])