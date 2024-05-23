from collections import deque
N = int(input())
r1,c1,r2,c2 = map(int,input().split())
INF = 1e9
dist = [[INF for _ in range(N)] for _ in range(N)]

dx = [2,2,0,0,-2,-2]
dy = [1,-1,2,-2,1,-1]

q = deque()
q.append((r1,c1))
dist[c1][r1] = 0
while q:
    a,b = q.popleft()
    for i in range(6):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<N and 0<=ny<N and dist[ny][nx] > dist[b][a] +1:
            dist[ny][nx] = dist[b][a] +1
            q.append((nx,ny))
if dist[c2][r2] == INF:
    print(-1)
else:
    print(dist[c2][r2])