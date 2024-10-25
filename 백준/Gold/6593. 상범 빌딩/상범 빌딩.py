from collections import deque
import sys

dl = [0,0,0,0,1,-1]
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]

while True:
    L,Y,X = map(int,input().split())
    building = [[] for _ in range(L)]
    if L == Y == X == 0:
        break
    for l in range(L):
        for _ in range(Y):
            building[l].append(list(input()))
        # 빈 줄 읽기
        sys.stdin.readline()
    for l in range(L):
        for y in range(Y):
            for x in range(X):
                if building[l][y][x] == "S":
                    start_x = x
                    start_y = y
                    start_l = l
                elif building[l][y][x] == "E":
                    end_x = x
                    end_y = y
                    end_l = l
    time = [[[1e9 for _ in range(X)] for _ in range(Y)] for _ in range(L)]
    q = deque()
    q.append((start_x,start_y,start_l))
    time[start_l][start_y][start_x] = 0
    while q:
        x,y,l = q.popleft()
        for i in range(6):
            nl = dl[i] + l
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nl<L and 0<=nx<X and 0<=ny<Y and time[nl][ny][nx] > time[l][y][x] + 1 and building[nl][ny][nx] != "#":
                time[nl][ny][nx] = time[l][y][x] + 1
                q.append((nx,ny,nl))
    if time[end_l][end_y][end_x] == 1e9:
        print("Trapped!")
    else:
        print("Escaped in " + str(time[end_l][end_y][end_x]) + " minute(s).")