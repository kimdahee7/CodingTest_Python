import copy
N = int(input())
candy = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

global answer
answer = 0

def eat_candy(x1,y1,x2,y2,candy):
    global answer
    # 두 칸에 들어있는 사탕 교환
    temp = candy[y1][x1]
    candy[y1][x1] = candy[y2][x2]
    candy[y2][x2] = temp

    # 행에서 가장 긴 행 카운트
    max_count = 0
    for i in range(N):
        cnt = 1
        before_data = candy[i][0]
        for j in range(1,N):
            if before_data == candy[i][j]:
                cnt +=1
            else:
                before_data = candy[i][j]
                max_count = max(max_count, cnt)
                cnt = 1
        max_count = max(max_count, cnt)

    # 열에서 가장 긴 열 카운트
    for i in range(N):
        cnt = 1
        before_data = candy[0][i]
        for j in range(1,N):
            if before_data == candy[j][i]:
                cnt +=1
            else:
                before_data = candy[j][i]
                max_count = max(max_count, cnt)
                cnt = 1
        max_count = max(max_count,cnt)
    answer = max(answer,max_count)


for y in range(N):
    for x in range(N):
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and candy[y][x] != candy[ny][nx]:
                c_candy = copy.deepcopy(candy)
                eat_candy(x,y,nx,ny,c_candy)

print(answer)