def solution(land):
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if i == 0:
                dp[0][j] = land[0][j]
            elif j == 0:
                dp[i][j] = land[i][j] + max(dp[i-1][1],dp[i-1][2],dp[i-1][3])
            elif j == 1:
                dp[i][j] = land[i][j] + max(dp[i-1][0],dp[i-1][2],dp[i-1][3])
            elif j == 2: 
                dp[i][j] = land[i][j] + max(dp[i-1][1],dp[i-1][0],dp[i-1][3])
            else:
                dp[i][j] = land[i][j] + max(dp[i-1][1],dp[i-1][2],dp[i-1][0])
    return max(dp[len(land)-1])