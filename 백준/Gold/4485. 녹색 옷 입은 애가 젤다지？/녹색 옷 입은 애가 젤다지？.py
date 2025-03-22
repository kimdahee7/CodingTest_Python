import sys
input = sys.stdin.readline
import heapq

dx = [0,0,1,-1]
dy = [1,-1,0,0]
num = 0
while True:
    num += 1
    N = int(input())
    if N == 0:
        exit()
    graph = [list(map(int,input().split())) for _ in range(N)]
    dist = [[1e9 for _ in range(N)] for _ in range(N)]
    h = []
    heapq.heappush(h,(graph[0][0],0,0))
    dist[0][0] = graph[0][0]
    while h:
        r,x,y = heapq.heappop(h)
        if y == N-1 and x == N-1:
            print("Problem " + str(num) + ": " + str(r) )
            break
        if dist[y][x] < r:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and dist[ny][nx] > dist[y][x] + graph[ny][nx]:
                dist[ny][nx] = dist[y][x] + graph[ny][nx]
                heapq.heappush(h,(dist[ny][nx],nx,ny))