N = int(input())
power = list(map(int,input().split()))
happy = list(map(int,input().split()))
power = [0] + power
happy = [0] + happy
dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,101):
        # 뺄 수 있는 경우
        if power[i] <= j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-power[i]]+happy[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][99])