N = int(input())
#l = [list(map(int,input().split())) for i in range(N**2)]
dic = {}
for _ in range(N**2):
    s,a,b,c,d = map(int,input().split())
    if s not in dic:
        dic[s] = [a,b,c,d]
sit = [[0 for _ in range(N)] for _ in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in dic:
    s = i
    a,b,c,d = dic[i]
    can_sit = []
    for y in range(N):
        for x in range(N):
            # 자리가 비어있는 경우
            if sit[y][x] == 0:
                favorite = 0
                blank = 0
                for dir in range(4):
                    nx = dx[dir] + x
                    ny = dy[dir] + y
                    if 0<=nx<N and 0<=ny<N:
                        if sit[ny][nx] == 0:
                            blank +=1
                        elif sit[ny][nx] !=0 and sit[ny][nx] in [a,b,c,d]:
                            favorite +=1
                can_sit.append((favorite,blank,y,x))
            # 자리가 차 있는 경우
            else:
                continue
    can_sit.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    sit_y,sit_x = can_sit[0][2], can_sit[0][3]
    sit[sit_y][sit_x] = s

answer = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        for dir in range(4):
            nx = dx[dir] + x
            ny = dy[dir] + y
            if 0<=nx<N and 0<=ny<N and sit[ny][nx] in dic[sit[y][x]]:
                cnt +=1
        if cnt == 1:
            answer +=1
        elif cnt == 2:
            answer +=10
        elif cnt == 3:
            answer +=100
        elif cnt == 4:
            answer +=1000
print(answer)
