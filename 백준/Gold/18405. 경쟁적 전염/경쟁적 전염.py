from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time = [[1e9 for _ in range(N)] for _ in range(N)]
S,X,Y = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    while q:
        c,t,x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N:
                if graph[ny][nx] > c and time[ny][nx] >= t+1:
                    graph[ny][nx] = c
                    time[ny][nx] = t + 1
                    q.append((graph[ny][nx], t + 1, nx, ny))

q = deque()
for y in range(N):
    for x in range(N):
        if graph[y][x] != 0:
            q.append((graph[y][x],0, x, y))
            time[y][x] = 0
        else:
            graph[y][x] = 1e9
bfs()

if time[X-1][Y-1] <= S:
    print(graph[X-1][Y-1])
else:
    print(0)