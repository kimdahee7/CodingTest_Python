from collections import deque

N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and cheese[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny, nx))
            elif 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and cheese[ny][nx] == 1:
                visited[ny][nx] = 1
                cheese[ny][nx] = 0
                cnt +=1
    return cnt


total_count = 0
for i in range(N):
    for j in range(M):
        if cheese[i][j] == 1:
            total_count +=1

answer = []
while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    if total_count == 0:
        break
    else:
        cnt = bfs()
        total_count -= cnt
        answer.append(cnt)

print(len(answer))
print(answer[-1])