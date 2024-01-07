from collections import deque
N = int(input())
l = [list(map(int,input().split())) for _ in range(N)]
answer = []
graph = [[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if l[i][j] == 1:
      graph[i].append(j)

def bfs(n):
  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1

for i in range(N):
  visited = [0] * N
  bfs(i)
  answer.append(visited)

for i in range(N):
  for j in range(N):
    print(answer[i][j], end = " ")
  print()