from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = 1e9
dist = [INF] * (N + 1)
answer = []
for i in range(M):
  A,B = map(int,input().split())
  graph[A].append(B)
  graph[B].append(A)

def bfs(n):
  q = deque()
  q.append(n)
  dist[n] = 0
  while q:
    x = q.popleft()
    for i in graph[x]:
      if dist[i] > dist[x] + 1:
        dist[i] = dist[x] + 1
        q.append(i)

for i in range(1,N+1):
  dist = [INF] * (N + 1)
  bfs(i)
  answer.append(sum(dist[1:N+1]))
print(answer.index(min(answer))+1)