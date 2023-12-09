dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1

T = int(input())
for _ in range(T):
  n = int(input())

  for i in range(3,n):
    dp[i] = dp[i-3] + dp[i-2]
  print(dp[n-1])