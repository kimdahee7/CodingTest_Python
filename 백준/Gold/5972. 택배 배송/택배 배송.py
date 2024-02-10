import heapq

N,M = map(int,input().split())
INF = 1e9
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for i in range(M):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
  
q = []
heapq.heappush(q,(1,0))
dist[1] = 0
while q:
  p,t = heapq.heappop(q)
  for i in graph[p]:
    if dist[i[0]] > dist[p] + i[1]:
      dist[i[0]] = dist[p] + i[1]
      heapq.heappush(q,(i[0],i[1]))
print(dist[N])