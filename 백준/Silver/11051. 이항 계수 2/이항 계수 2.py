N,K = map(int,input().split())
dp = [[] for _ in range(N+1)]

for i in range(1,N+2):
    dp[i-1] = [0 for _ in range(i)]

for i in range(N+1):
    for j in range(i+1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[N][K]%10007)