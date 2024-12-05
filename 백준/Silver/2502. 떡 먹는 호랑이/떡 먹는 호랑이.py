D,K = map(int,input().split())
for i in range(1,K+1):
    dp = [0] * (D + 1)
    dp[1] = i
    for j in range(1,K+1):
        dp[2] = j
        for k in range(3,D+1):
            dp[k] = dp[k-1] + dp[k-2]
        if dp[D] == K:
            print(i)
            print(j)
            exit()