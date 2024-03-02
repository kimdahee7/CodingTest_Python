from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
  graph[i].append(int(input()))

def bfs(n):
  visited = [False] * (N+1)
  q = deque()
  q.append(n)
  total = [n]
  k = [graph[n][0]]
  visited[n] = True
  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        total.append(i)
        k.append(graph[i][0])
  k.sort()
  total.sort()
  if k == total:
    return total
  else:
    return []

answer = []
for i in range(1,N+1):
  result = bfs(i)
  if result:
    answer.append(result)

s = set()
for i in answer:
  for j in i:
    s.add(j)

s = sorted(s)
print(len(s))
for i in s:
  print(i)