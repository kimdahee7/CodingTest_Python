N,M = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
dp = [[[1e9 for _ in range(3)] for _ in range(M)] for _ in range(N)]

# 왼쪽 아래 0 / 아래 1 / 오른쪽 아래 2
for i in range(M):
    for j in range(3):
        dp[0][i][j] = map[0][i]

for i in range(1,N):
    for j in range(M):
        for k in range(3):
            if j ==0 and k ==2:
                continue
            if j == M-1 and k == 0:
                continue
            if k == 0:
                dp[i][j][k] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + map[i][j]
            elif k == 1:
                dp[i][j][k] = min(dp[i-1][j][0],dp[i-1][j][2]) + map[i][j]
            else:
                dp[i][j][k] = min(dp[i-1][j-1][0],dp[i-1][j-1][1]) + map[i][j]

answer = 1e9
for i in dp[-1]:
    answer = min(answer,min(i))
print(answer)