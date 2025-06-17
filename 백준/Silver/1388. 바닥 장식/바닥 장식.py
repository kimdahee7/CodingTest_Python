from collections import deque
N,M = map(int,input().split())
floor = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
def bfs(y,x):
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<M and 0<=ny<N and visited[ny][nx] == 0:
                if floor[y][x] == floor[ny][nx] == "-":
                    if i == 0 or i == 1:
                        visited[ny][nx] = 1
                        q.append((ny,nx))
                elif floor[y][x] == floor[ny][nx] == "|":
                    if i == 2 or i ==3:
                        visited[ny][nx] = 1
                        q.append((ny, nx))
result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            bfs(i,j)
            result += 1
print(result)