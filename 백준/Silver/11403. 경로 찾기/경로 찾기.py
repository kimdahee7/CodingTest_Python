from collections import deque
N = int(input())
m = [list(map(int,input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if m[i][j] == 1:
      graph[i].append(j)

def bfs(n,visited):
  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        visited[i] = 1
        q.append(i)

answer = []
for i in range(N):
  visited = [0] * N
  bfs(i,visited)
  answer.append(visited)

for i in range(N):
  for j in range(N):
    print(answer[i][j],end=" ")
  print()