import heapq

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

h = []
heapq.heappush(h,(0,0,0))
visited[0][0] = 1
while h:
    c,a,b = heapq.heappop(h)
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx == n-1 and ny == n-1:
            print(c)
            exit()
        elif 0<=nx<n and 0<=ny<n and visited[ny][nx] == 0:
            if graph[ny][nx] == "0":
                visited[ny][nx] = 1
                heapq.heappush(h,(c+1,nx,ny))
            else:
                visited[ny][nx] = 1
                heapq.heappush(h,(c,nx,ny))