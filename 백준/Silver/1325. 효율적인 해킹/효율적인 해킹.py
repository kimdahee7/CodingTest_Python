from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  A,B = map(int,input().split())
  graph[B].append(A)

def bfs(n):
  visited = [0] * (N + 1)
  q = deque()
  q.append(n)
  visited[n] = 1
  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        visited[i] = 1
        q.append(i)
  return visited.count(1)

answer = []
for i in range(1,N+1):
  answer.append(bfs(i))
max_data = max(answer)
for i in range(N):
  if answer[i] == max_data:
    print(i+1, end=" ")