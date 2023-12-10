from collections import deque
F,S,G,U,D = map(int,input().split())

dx = [U,-D]
visited = [1 for _ in range(F+1)]
result = [0 for _ in range(F+1)]

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == G:
            print(result[x])
        for i in range(2):
            nx = x + dx[i]
            if 0<nx<=F and visited[nx] == 1:
                q.append(nx)
                visited[nx] = 0
                result[nx] = result[x] +1
    if result[G] == 0:
      print("use the stairs")
if S == G:
  print(0)
else:
  bfs(S)