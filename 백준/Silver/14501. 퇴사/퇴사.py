N = int(input())
dp = [0] * N
l = []
for _ in range(N):
  t = list(map(int,input().split()))
  l.append(t)
for i in range(N):
  if l[i][0] + (i + 1) <= N+1:
    dp[i] = l[i][1]
  for j in range(i):
    if l[j][0] + (j+1) <= (i+1) and (i+1)+l[i][0] <= N+1:
      dp[i] = max(dp[i],dp[j]+l[i][1])
print(max(dp))