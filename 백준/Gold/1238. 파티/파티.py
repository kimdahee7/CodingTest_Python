import heapq

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
answer = []
INF = 1e9
for _ in range(M):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  
def dikstra(start,dist):
  q = []
  heapq.heappush(q,(start,0))
  dist[start] = 0
  while q:
    p,t = heapq.heappop(q)
    for i in graph[p]:
      if dist[i[0]] > dist[p] + i[1]:
        dist[i[0]] = dist[p] + i[1]
        heapq.heappush(q,(i[0],i[1]))
  
for i in range(1,N+1):
  dist = [INF] * (N+1)
  dikstra(i,dist)
  answer.append(dist[X])
dist = [INF] * (N+1)
dikstra(X,dist)
for i in range(1,len(dist)):
  answer[i-1] = answer[i-1] + dist[i]
print(max(answer))