import sys
from collections import deque

q = deque()

input = sys.stdin.readline
def main():
  N,M = map(int,input().split())
  graph = [[] for i in range(N+1)]
  visited = [False] * (N+1)
  total = 0
  for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
 
  for j in range(1,N+1):
    if visited[j] == False:
      total += 1
      q.append(j)
      while len(q):
        current = q.popleft()
        for to in graph[current]:
          if not visited[to]:
            visited[to] = True
            q.append(to)
  print(total)

main()
  
