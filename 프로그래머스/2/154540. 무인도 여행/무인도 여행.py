from collections import deque
def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(bfs(j,i,maps,visited))
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,maps,visited):
    total = 0
    q = deque()
    q.append((x,y))
    visited[y][x] = 1
    total += int(maps[y][x])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps) and maps[ny][nx] != "X" and visited[ny][nx] == 0:
                q.append((nx,ny))
                visited[ny][nx] = 1
                total += int(maps[ny][nx])
    return total
        