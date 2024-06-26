def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if [j+1,i+1] not in puddles:
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n-1][m-1]