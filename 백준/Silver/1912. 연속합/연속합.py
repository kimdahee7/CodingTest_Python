N = int(input())
l = list(map(int,input().split()))

dp = [0] * N
dp[0] = l[0]
for i in range(1,N):
  dp[i] = max(dp[i-1]+l[i],l[i])
print(max(dp))