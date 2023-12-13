from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()

def bfs():
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<M and 0<=ny<N and graph[ny][nx] ==0:
        count[ny][nx] = count[b][a] +1
        q.append((nx,ny))
        graph[ny][nx] = 1

M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
count = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      q.append((j,i))

bfs()

result = -1
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      print(-1)
      exit(0)
for i in count:
  max_c = max(i)
  result = max(result, max_c)
print(result)
