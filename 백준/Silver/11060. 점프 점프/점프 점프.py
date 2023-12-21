from collections import deque
N = int(input())
l = list(map(int,input().split()))

INF = 1e9
dist = [INF] * (N)

def bfs():
  q = deque()
  q.append(0)
  dist[0] = 0
  while q:
    a = q.popleft()
    if a == N-1:
      break
    for i in range(1,l[a]+1):
      if 0<=a+i<=N-1:
        if dist[a+i] > dist[a] +1:
          dist[a+i] = dist[a] +1
          q.append(a+i)
bfs()
if dist[N-1] == INF:
  print(-1)
else:
  print(dist[N-1])