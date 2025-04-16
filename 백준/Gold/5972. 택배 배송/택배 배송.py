import heapq

def dijk(start):
    h = []
    heapq.heappush(h,(0,start))
    dist[start] = 0
    while h:
        d,now = heapq.heappop(h)
        if dist[now] < d:
            continue
        for i in route[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(h,(cost,i[0]))

N,M = map(int,input().split())
route = [[] for _ in range(N+1)]
dist = [1e9 for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    route[a].append((b,c))
    route[b].append((a,c))

dijk(1)
print(dist[N])