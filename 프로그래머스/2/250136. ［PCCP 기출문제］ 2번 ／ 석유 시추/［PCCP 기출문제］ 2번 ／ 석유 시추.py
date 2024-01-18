from collections import deque

def solution(land):
    answer = 0
    M = len(land[0])
    N = len(land)
    dp = [0] * (M+1)
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                bfs(j,i,land,dp,M,N)
    answer = max(dp)
    return answer

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,land,dp,M,N):
    l = set()
    q = deque()
    q.append((x,y))
    land[y][x] = 0
    l.add(x)
    total = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<M and 0<=ny<N and land[ny][nx] == 1:
                total +=1
                q.append((nx,ny))
                l.add(nx)
                land[ny][nx] = 0
    for k in l:
        dp[k] += total
    
        
