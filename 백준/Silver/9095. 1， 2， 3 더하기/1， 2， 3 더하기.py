dp = [0] * 11
dp[0] = 1
dp[1] = 2
dp[2] = 4

T = int(input())
for i in range(T):
  n = int(input())
  
  for i in range(3,n):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
  print(dp[n-1])