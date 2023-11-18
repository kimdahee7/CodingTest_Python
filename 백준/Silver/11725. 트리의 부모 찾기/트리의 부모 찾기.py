import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
     
N = int(input())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
for i in range(N-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph,n,visited):
  visited[n] = True
  for i in graph[n]:
    if not visited[i]:
      answer[i] = n
      dfs(graph,i,visited)

dfs(graph,1,visited)

for i in range(2,N+1):
  print(answer[i])
