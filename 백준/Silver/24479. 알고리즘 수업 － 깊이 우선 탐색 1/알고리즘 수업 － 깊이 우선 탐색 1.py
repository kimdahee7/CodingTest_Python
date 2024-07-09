import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

global k
k = 1
def dfs(start):
    global k
    visited[start] = k
    k +=1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
dfs(R)
for i in range(1,N+1):
    print(visited[i])