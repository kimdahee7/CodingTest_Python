from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF =1e9
dist = [INF] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
dist[1] = 0
while q:
    x = q.popleft()
    for i in graph[x]:
        if dist[i] > dist[x] +1:
            dist[i] = dist[x] +1
            q.append(i)

max_data = max(dist[1:N+1])
for i in range(1,N+1):
    if dist[i] == max_data:
        print(i,end = " ")
        break
print(max_data, end = " ")
print(dist.count(max_data))