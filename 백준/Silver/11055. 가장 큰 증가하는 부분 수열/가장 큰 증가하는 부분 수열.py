N = int(input())
ball = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
  dp[i] = ball[i]
for i in range(1,len(ball)):
  for j in range(i):
    if ball[j] < ball[i]:
      dp[i] = max(dp[i],dp[j] + ball[i])
print(max(dp))