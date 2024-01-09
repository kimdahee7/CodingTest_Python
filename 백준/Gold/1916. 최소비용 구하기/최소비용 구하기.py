import heapq
N = int(input())
M = int(input())
INF = 1e9
graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
for i in range(M):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
start,end = map(int,input().split())

q = []
heapq.heappush(q,(0,start))
dist[start] = 0
while q:
  d,now = heapq.heappop(q)
  if dist[now] < d:
    continue
  for i in graph[now]:
    if dist[i[0]] > d + i[1]:
      dist[i[0]] = d + i[1]
      heapq.heappush(q,(d+i[1],i[0]))

print(dist[end])