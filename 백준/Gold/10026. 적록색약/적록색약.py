from collections import deque
N = int(input())
RGB = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,color,visited):
    q = deque()
    q.append((x, y))
    visited[y][x] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N and RGB[ny][nx] == color and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((nx,ny))

#적록색약이 아닌 사람
total_1 = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            total_1 +=1
            if RGB[i][j] == "R":
                bfs(j,i,"R",visited)
            elif RGB[i][j] == "G":
                bfs(j,i,"G",visited)
            else:
                bfs(j,i,"B",visited)

for i in range(N):
    for j in range(N):
        if RGB[i][j] == "G":
            RGB[i][j] = "R"
#적록색약인 사람
total_2 = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            total_2 +=1
            if RGB[i][j] == "R":
                bfs(j,i,"R",visited)
            else:
                bfs(j,i,"B",visited)
print(total_1, total_2)