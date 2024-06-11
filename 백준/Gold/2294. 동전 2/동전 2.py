N,K = map(int,input().split())
coin = set()
for _ in range(N):
    value = int(input())
    coin.add(value)
    
INF = 1e9

dp = [INF for _ in range(100001)]
for i in coin:
    dp[i] = 1

for i in range(1,K+1):
    if dp[i] == INF:
        for j in range(1,i//2+1):
            dp[i] = min(dp[i],dp[j] + dp[i-j])

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])