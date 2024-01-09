import heapq

V,E = map(int,input().split())
K = int(input())
INF = 1e9
graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
for _ in range(E):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))

q = []
heapq.heappush(q,(0,K))
dist[K] = 0
while q:
  d,now = heapq.heappop(q)
  if dist[now] < d:
    continue
  for i in graph[now]:
    if dist[i[0]] > i[1] + d:
      dist[i[0]] = i[1] + d
      heapq.heappush(q,(i[1] + d,i[0]))

for i in range(1,V+1):
  if dist[i] == INF:
    print("INF")
  else:
    print(dist[i])