import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
map = [input() for _ in range(N)]
word = input().strip()
# 방문한 경로 확인
dp = [[[-1 for _ in range(len(word))] for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 0

def dfs(x, y, index):
    if index == len(word) - 1:
        return 1
    if dp[y][x][index] != -1:
        return dp[y][x][index]
    dp[y][x][index] = 0
    for i in range(4):
        for j in range(1, K + 1):
            nx = x + (dx[i] * j)
            ny = y + (dy[i] * j)
            if 0 <= nx < M and 0 <= ny < N and index + 1 < len(word) and map[ny][nx] == word[index + 1]:
                dp[y][x][index] += dfs(nx,ny,index+1)
    return dp[y][x][index]

for i in range(N):
    for j in range(M):
        if map[i][j] == word[0]:
            answer += dfs(j,i,0)

print(answer)