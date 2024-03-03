N = int(input())
line = [int(input()) for _ in range(N)]
dp = [1] * N
count = 0
for i in range(1,N):
  for j in range(i):
    if line[i] > line[j]:
      dp[i] = max(dp[j]+1, dp[i])
print(N-max(dp))