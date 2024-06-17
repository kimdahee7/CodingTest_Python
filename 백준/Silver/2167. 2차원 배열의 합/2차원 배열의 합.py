N,M = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(N)]
K = int(input())
sum = [[0 for _ in range(M+1)] for _ in range(N+1)]
sum[1][1] = l[0][0]

for i in range(2,M+1):
    sum[1][i] = sum[1][i-1] + l[0][i-1]
for i in range(2,N+1):
    sum[i][1] = sum[i-1][1] + l[i-1][0]

for i in range(2,N+1):
    for j in range(2,M+1):
        sum[i][j] = l[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

for _ in range(K):
    i,j,x,y = map(int,input().split())
    print(sum[x][y] - sum[x][j-1] - sum[i-1][y] + sum[i-1][j-1])