from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    INF = 1e9
    dist = [[INF for _ in range(m)]for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    dist[0][0] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                if dist[nx][ny] > dist[a][b] +1:
                    dist[nx][ny] = dist[a][b] +1
                    q.append((nx,ny))
    if dist[n-1][m-1] == INF:
        answer = -1
    else:
        answer = dist[n-1][m-1]
    return answer