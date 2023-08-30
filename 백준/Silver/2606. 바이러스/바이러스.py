import sys
input = sys.stdin.readline
from collections import deque
def main(): 
  n = int(input())
  c = int(input())
  graph = [[] for _ in range(n+1)]
  for i in range(c):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in range(1,n+1):
    graph[i].sort()
  visited = [False] * (n+1)
  print(BFS(graph,1,visited)-1)

def BFS(graph,v,visited):
  total = 0
  queue = deque([v])
  visited[v] = True

  while queue:
    v = queue.popleft()
    total +=1
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
  return total
main()