from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

q = deque()
def bfs(x,y,cnt):
    result = []
    q.append((x,y,cnt))
    visited[y][x] = 1
    while q:
        a,b,c = q.popleft()
        if graph[b][a] == 1:
            result.append(c)
        for i in range(8):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0<=nx<M and 0<=ny<N and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((nx, ny, c + 1))
    return result

answer = []
for y in range(N):
    for x in range(M):
        safe_dist = 0
        if graph[y][x] == 0:
            visited = [[0 for _ in range(M)] for _ in range(N)]
            safe_dist = min(bfs(x,y,0))
            answer.append(safe_dist)
print(max(answer))