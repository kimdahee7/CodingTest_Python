import heapq

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
INF = 1e9
dist = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    bus[a].append((b,c))
start, end = map(int,input().split())

h = []
heapq.heappush(h,(0,start))
while h:
    c, now = heapq.heappop(h)
    if dist[now] < c:
        continue
    for i in bus[now]:
        cost = c + i[1]
        if cost < dist[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(h,(cost,i[0]))
print(dist[end])