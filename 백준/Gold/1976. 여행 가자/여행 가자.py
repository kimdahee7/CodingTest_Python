from collections import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
m = [list(map(int,input().split())) for _ in range(N)]
t = list(map(int,input().split()))
for i in range(N):
  for j in range(N):
    if m[i][j] == 1:
      graph[i+1].append(j+1)

def bfs(n,d):
  visited = [False] * (N+1)
  q = deque()
  q.append(n)
  visited[n] = True
  while q:
    a = q.popleft()
    if a == d:
      return 1
    for i in graph[a]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
  return 0
  
answer = 0
for i in range(len(t)-1):
  b = bfs(t[i],t[i+1])
  if b == 1:
    answer +=1
  else:
    print("NO")
    exit()
if answer == len(t)-1:
  print("YES")