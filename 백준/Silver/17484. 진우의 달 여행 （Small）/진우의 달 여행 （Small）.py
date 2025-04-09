N,M = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(N)]

dp = [[[1e9,1e9,1e9] for _ in range(M)] for _ in range(N)]
for i in range(M):
    for j in range(3):
        dp[0][i][j] = space[0][i]

for i in range(1,N):
    for j in range(M):
        if j == 0:
            dp[i][j][1] = min(dp[i][j][1],space[i][j] + dp[i-1][j][0], space[i][j] + dp[i-1][j][2])
            dp[i][j][0] = min(dp[i][j][0],space[i][j] + dp[i-1][j+1][1], space[i][j] + dp[i-1][j+1][2])
        elif j == M-1:
            dp[i][j][1] = min(dp[i][j][1],space[i][j] + dp[i-1][j][0], space[i][j] + dp[i-1][j][2])
            dp[i][j][2] = min(dp[i][j][2],space[i][j] + dp[i-1][j-1][1], space[i][j] + dp[i-1][j-1][0])
        else:
            dp[i][j][0] = min(dp[i][j][0],space[i][j] + dp[i-1][j+1][1], space[i][j] + dp[i-1][j+1][2])
            dp[i][j][1] = min(dp[i][j][1],space[i][j] + dp[i-1][j][0], space[i][j] + dp[i-1][j][2])
            dp[i][j][2] = min(dp[i][j][2],space[i][j] + dp[i-1][j-1][1], space[i][j] + dp[i-1][j-1][0])
answer = 1e9
for i in dp[-1]:
    answer = min(answer,min(i))
print(answer)