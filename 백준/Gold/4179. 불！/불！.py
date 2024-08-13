from collections import deque

R,C = map(int,input().split())
map = [list(input()) for _ in range(R)]
time = [[1e9 for _ in range(C)] for _ in range(R)]
visited = [[1e9 for _ in range(C)] for _ in range(R)]

q = deque()
q1 = deque()

for i in range(R):
    for j in range(C):
        if map[i][j] == "F":
            q.append((j,i))
            time[i][j] = 0
        elif map[i][j] == "J":
            q1.append((j,i,1))
            visited[i][j] = 1


dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<=ny<R and map[ny][nx] == "." and time[ny][nx] == 1e9:
            time[ny][nx] = time[y][x] + 1
            q.append((nx,ny))
while q1:
    x,y,k = q1.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<=ny<R and map[ny][nx] == "." and visited[ny][nx] == 1e9 and time[ny][nx] > k:
            q1.append((nx,ny,k+1))
            visited[ny][nx] = k+1

answer = 1e9
for i in range(R):
    for j in range(C):
        if i ==0 or j ==0 or i ==R-1 or j == C-1:
            answer = min(answer,visited[i][j])
if answer != 1e9:
    print(answer)
else:
    print("IMPOSSIBLE")