N = int(input())
l = list(map(int,input().split()))
dp = [[0] * 21 for i in range(N)]

dp[0][l[0]] = 1

for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            if 0<=j + l[i] < 21:
                dp[i][j + l[i]] += dp[i-1][j]
            if 0<=j - l[i] < 21:
                dp[i][j - l[i]] += dp[i-1][j]

print(dp[N-2][l[-1]])