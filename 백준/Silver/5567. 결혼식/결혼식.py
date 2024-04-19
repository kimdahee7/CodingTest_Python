from collections import deque
N = int(input())
m = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
answer = 0
visited[1] = 1
for i in graph[1]:
  q.append(i)
  answer += 1
  visited[i] = 1

while q:
  x = q.popleft()
  for i in graph[x]:
    if not visited[i]:
      visited[i] = 1
      answer +=1
print(answer)