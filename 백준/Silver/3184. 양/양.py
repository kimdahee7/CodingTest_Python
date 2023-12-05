from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  w = 0
  s = 0
  q = deque()
  q.append((x,y))
  if graph[y][x] == "v":
    w+=1
  elif graph[y][x] == "o":
    s+=1
  graph[y][x] = "#"
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<=nx<C and 0<=ny<R and graph[ny][nx] != "#":
        if graph[ny][nx] == "v":
          w +=1
        elif graph[ny][nx] == "o":
          s +=1
        graph[ny][nx] = "#"
        q.append((nx,ny))
  if s > w:
    return s, 0
  else:
    return 0, w

R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]

total_s = 0
total_w = 0

for i in range(R):
  for j in range(C):
    if graph[i][j] == "v" or graph[i][j] == "o":
      c_s, c_w = bfs(j,i)
      total_s +=c_s
      total_w +=c_w
print(total_s,total_w)  