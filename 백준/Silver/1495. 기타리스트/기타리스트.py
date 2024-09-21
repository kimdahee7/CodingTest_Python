N,S,M = map(int,input().split())
V = list(map(int,input().split()))
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = 1

for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j] != 0:
            if 0<= j+V[i-1] <= M:
                dp[i][j+V[i-1]] = 1
            if 0<= j-V[i-1]<= M:
                dp[i][j-V[i-1]] = 1
answer = -1
for i in range(M,-1,-1):
    if dp[N][i] == 1:
        answer = i
        break
print(answer)