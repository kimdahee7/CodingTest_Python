import heapq
def solution(n, edge):
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    q = []
    heapq.heappush(q,(0,1))
    dist[1] = 0
    while q:
        d,now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            if dist[i] > d + 1:
                dist[i] = d + 1
                heapq.heappush(q,(d+1,i))
    dist[0] = 0
    max_data = max(dist)
    answer = dist.count(max_data)
    return answer