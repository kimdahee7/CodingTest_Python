import sys
input = sys.stdin.readline
from collections import deque
def main(): 
  N,M,V = map(int,input().split())
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in range(1,N+1):
    graph[i].sort()
  visited = [False] * (N+1)
  DFS(graph,V,visited)
  print()
  visited = [False] * (N+1)
  BFS(graph,V,visited)

def DFS(graph,v,visited):
  visited[v] = True
  print(v,end=" ")
  for i in graph[v]:
    if not visited[i]:
      DFS(graph,i,visited)

def BFS(graph,v,visited):
  queue = deque([v])
  visited[v] = True

  while queue:
    v = queue.popleft()
    print(v,end=" ")
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
main()