N = int(input())
pipe = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

#0-가로, 1-대각선, 2-아래
for i in range(N):
    for j in range(1,N):
        if i == 0 and pipe[i][j] == 0:
            dp[i][j][0] = 1
        else:
            break

for i in range(1,N):
    for j in range(1,N):
        if pipe[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
        if pipe[i][j] == 0 and pipe[i-1][j] == 0 and pipe[i][j-1] == 0:
            dp[i][j][1] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][2] + dp[i - 1][j - 1][1]

print(sum(dp[N-1][N-1]))