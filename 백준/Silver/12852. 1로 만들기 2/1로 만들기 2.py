N = int(input())
dp = [0] * (N+1)
result = []
for i in range(2,N+1):
  dp[i] = dp[i-1] +1
  if i % 2 == 0:
    dp[i] = min(dp[i],dp[i//2]+1)
  if i % 3 == 0:
    dp[i] = min(dp[i],dp[i//3]+1)

print(dp[N])
result = [N]
start = dp[N]
for i in range(N,0,-1):
  if dp[i] < start:
    if i+1 == N or i*2 == N or i*3 == N:
      result.append(i)
      start = dp[i]
      N = i
for i in result:
  print(i, end=" ")