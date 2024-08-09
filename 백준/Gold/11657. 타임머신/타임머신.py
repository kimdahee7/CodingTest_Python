N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = 1e15
dist = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dist[1] = 0
check = False

for i in range(1,N+1):
    for u in range(1,N+1):
        if dist[u] == INF: continue;
        for v,c in graph[u]:
            if dist[v] > c + dist[u]:
                if i == N:
                    check = True
                else:
                    dist[v] = c + dist[u]

if check == True:
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
