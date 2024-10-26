N,M,R = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]

for r in range(R):
    for i in range(min(N,M)//2):
        x,y = i, i
        temp = m[y][x]
        # 왼쪽
        for j in range(y+1,N-y):
            before_data = m[j][x]
            m[j][x] = temp
            temp = before_data
        # 아래
        for j in range(x+1,M-x):
            before_data = m[N-1-y][j]
            m[N-1-y][j] = temp
            temp = before_data
        # 오른쪽
        for j in range(N-y-2,y-1,-1):
            before_data = m[j][M-1-x]
            m[j][M-1-x] = temp
            temp = before_data
        # 위
        for j in range(M-x-2,x-1,-1):
            before_data = m[y][j]
            m[y][j] = temp
            temp = before_data
for i in range(N):
    for j in range(M):
        print(m[i][j],end=" ")
    print()