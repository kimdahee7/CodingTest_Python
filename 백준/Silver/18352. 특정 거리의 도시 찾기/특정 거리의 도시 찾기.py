from collections import deque
N,M,K,X = map(int,input().split())
INF = 1e9
graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
  A,B = map(int,input().split())
  graph[A].append(B)

q = deque()
q.append(X)
dist[X] = 0
while q:
  x = q.popleft()
  for i in graph[x]:
    if not visited[i]:
      dist[i] = min(dist[i],dist[x]+1)
      q.append(i)
      visited[i] = True
answer = []
for i in range(len(dist)):
  if dist[i] == K:
    answer.append(i)
if len(answer) == 0:
  print(-1)
else:
  for i in answer:
    print(i)