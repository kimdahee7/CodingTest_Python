from collections import deque
T = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(T):
    W,H = map(int,input().split())
    m = [list(input()) for _ in range(H)]
    visited = [[1e9 for _ in range(W)] for _ in range(H)]
    time = [[1e9 for _ in range(W)] for _ in range(H)]
    q_f = deque()
    q = deque()
    answer = 1e9
    for y in range(H):
        for x in range(W):
            if m[y][x] == "@":
                # 상근이의 시작 위치
                q.append((x,y,1))
                visited[y][x] = 1
            elif m[y][x] == "*":
                # 불의 시작 위치
                q_f.append((x,y))
                time[y][x] = 1
    while q_f:
        x,y = q_f.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<W and 0<=ny<H and time[ny][nx] == 1e9 and m[ny][nx] == ".":
                time[ny][nx] = time[y][x] + 1
                q_f.append((nx,ny))

    while q:
        x,y,t = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < W and 0 <= ny < H and visited[ny][nx] == 1e9 and time[ny][nx] > t+1 and m[ny][nx] == ".":
                visited[ny][nx] = t + 1
                q.append((nx,ny,t+1))

    for i in range(H):
        for j in range(W):
            if visited[i][j] != 1e9:
                if i == 0 or j == 0 or i == H-1 or j == W-1:
                    answer = min(answer,visited[i][j])

    if answer == 1e9:
        print("IMPOSSIBLE")
    else:
        print(answer)

