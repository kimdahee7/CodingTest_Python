from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
INF = 1e9
c = 0
while True:
  c +=1
  N = int(input())
  if N == 0:
    break
  graph = [list(map(int,input().split())) for _ in range(N)]
  dist = [[INF for _ in range(N)] for _ in range(N)]
  q = deque()
  q.append((0,0))
  dist[0][0] = graph[0][0]
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<N and 0<=ny<N:
        if dist[ny][nx] > dist[b][a] + graph[ny][nx]:
          dist[ny][nx] = dist[b][a] + graph[ny][nx]
          q.append((nx,ny))
  print("Problem "+str(c)+": "+str(dist[N-1][N-1]))