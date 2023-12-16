from collections import deque

A,B,N,M = map(int,input().split())
graph = [0] * 100001
q = deque()
q.append(N)

while q:
  x = q.popleft()
  if x == M:
    print(graph[M])
    break
  for i in (x+1,x-1,x+A,x+B,x-A,x-B,x*A,x*B):
    if 0<=i<100001 and graph[i] == 0:
      graph[i] = graph[x] +1
      q.append(i)