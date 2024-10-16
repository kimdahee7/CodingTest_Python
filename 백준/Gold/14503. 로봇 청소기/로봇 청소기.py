N,M = map(int,input().split())
y,x,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
op = [2, 3, 0, 1]

cnt = 0
while True:
    if graph[y][x] == 0:
        graph[y][x] = 2
        cnt +=1
    check = False
    for dir in range(4):
        nx = dx[dir] + x
        ny = dy[dir] + y
        if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 0:
            check = True
            break
    # 빈 칸이 없는 경우
    if not check:
        nx = dx[op[d]] + x
        ny = dy[op[d]] + y
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] != 1:
            x, y = nx, ny
        else:
            break
    # 빈 칸이 있는 경우
    else:
        d = (d - 1 + 4) % 4
        nx = dx[d] + x
        ny = dy[d] + y
        if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 0:
            x, y = nx, ny
print(cnt)


