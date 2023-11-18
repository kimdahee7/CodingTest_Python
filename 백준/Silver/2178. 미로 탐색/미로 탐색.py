import sys
from collections import deque
input = sys.stdin.readline

INF = 1e9

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N,M = map(int,input().split())

graph = [input() for _ in range(N)]
q = deque()

dist = [[INF for _ in range(M)] for _ in range(N)]

dist[0][0] = 0
q.append((0, 0))

while len(q):
  (y, x) = q.popleft()
  for dir in range(4):
    ny = y + dy[dir]
    nx = x + dx[dir]

    if ny >= N or ny < 0 or nx >= M or nx < 0:
      continue

    if graph[ny][nx] == '0':
      continue

    if dist[ny][nx] > dist[y][x] + 1:
      dist[ny][nx] = dist[y][x] + 1
      q.append((ny,nx))

print(dist[N-1][M-1] + 1)

      

  
