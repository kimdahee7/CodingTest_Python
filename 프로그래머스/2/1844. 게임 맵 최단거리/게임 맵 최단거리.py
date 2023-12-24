from collections import deque
def solution(maps):
    answer = 0
    n = len(maps[0]) #열
    m = len(maps) #행
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    INF = 1e9
    dist = [[INF for _ in range(n)] for _ in range(m)]
    
    q = deque()
    q.append((0,0))
    dist[0][0] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[ny][nx] == 1:
                if dist[ny][nx] > dist[b][a] + 1:
                    dist[ny][nx] = dist[b][a] + 1
                    q.append((nx,ny))
    if dist[m-1][n-1] == INF:
        answer = -1
    else:
        answer = dist[m-1][n-1]
    return answer

    