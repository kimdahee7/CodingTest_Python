N = int(input())
dp= [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
  for j in range(len(dp[i])):
    if j == 0:
      dp[i][j] += min(dp[i-1][1],dp[i-1][2])
    elif j == 1:
      dp[i][j] += min(dp[i-1][0],dp[i-1][2])
    else:
      dp[i][j] += min(dp[i-1][0],dp[i-1][1])
print(min(dp[N-1]))