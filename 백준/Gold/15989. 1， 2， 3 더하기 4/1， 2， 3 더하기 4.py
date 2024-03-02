T = int(input())
dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
for _ in range(T):
  n = int(input())
  if n <= 3:
    print(dp[n])
  else:
    for i in range(4,n+1):
      dp[i] = dp[i-3] + (i//2) +1
    print(dp[n])