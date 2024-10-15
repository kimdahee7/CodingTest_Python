N = int(input())
P = list(map(int,input().split()))
dp = [0] * (N+1)
for i in range(N):
    dp[i+1] = P[i]

for i in range(2,N+1):
    for j in range(i):
        dp[i] = min(dp[j] + dp[i-j],dp[i])
print(dp[N])