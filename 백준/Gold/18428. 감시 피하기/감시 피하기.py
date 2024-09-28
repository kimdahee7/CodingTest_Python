N = int(input())
map = [list(map(str,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(map):
    for i in range(N):
        for j in range(N):
            if map[i][j] == "T":
                for k in range(4):
                    nx = i
                    ny = j
                    while 0<=nx<N and 0<=ny<N:
                        if map[nx][ny] == "S":
                            return False
                        if map[nx][ny] == "O":
                            break
                        nx += dx[k]
                        ny += dy[k]
    return True

def backtracking(cnt):
    if cnt == 3:
        if check(map):
            print("YES")
            exit()
    else:
        for i in range(N):
            for j in range(N):
                if map[i][j] == "X":
                    map[i][j] = "O"
                    backtracking(cnt + 1)
                    map[i][j] = "X"

backtracking(0)

print("NO")