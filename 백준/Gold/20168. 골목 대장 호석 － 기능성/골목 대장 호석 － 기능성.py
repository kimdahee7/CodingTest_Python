N,M,A,B,C = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result = []
def dfs(start,visited,money,MAX):
    if start == B:
        if money <= C:
            result.append((money,MAX))
        return
    for i in graph[start]:
        if not visited[i[0]]:
            before = MAX
            MAX = max(MAX,i[1])
            money += i[1]
            visited[i[0]] = 1
            dfs(i[0],visited,money,MAX)
            visited[i[0]] = 0
            money -= i[1]
            MAX = before

dfs(A,visited,0,0)
visited[A] = 1
result.sort(key=lambda x:x[1])
if len(result) == 0:
    print(-1)
else:
    print(result[0][1])