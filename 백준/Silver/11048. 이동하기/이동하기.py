N,M = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

visited[0][0] = map[0][0]

for i in range(1,M):
    visited[0][i] = visited[0][i-1] + map[0][i]
for i in range(1,N):
    visited[i][0] = visited[i-1][0] + map[i][0]

for i in range(1,N):
    for j in range(1,M):
        visited[i][j] = max(visited[i-1][j-1]+map[i][j], visited[i-1][j]+map[i][j], visited[i][j-1]+map[i][j])

print(visited[N-1][M-1])