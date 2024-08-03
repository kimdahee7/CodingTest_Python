N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

# 가로 0 / 세로 1 / 대각선 2
# 0행은 가로로만 이동 가능
dp[0][1][0] = 1
for i in range(2,N):
    if map[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1,N):
    for j in range(1,N):
        if map[i][j] == 0 and map[i-1][j] == 0 and map[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][1] + dp[i-1][j-1][0] + dp[i-1][j-1][2]
        if map[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[N-1][N-1]))