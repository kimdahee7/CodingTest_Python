from collections import deque
R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,cnt_v,cnt_k):
    q = deque()
    q.append((x,y))
    visited[y][x] = 1
    if graph[y][x] == "v":
        cnt_v +=1
    else:
        cnt_k +=1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0<=nx<C and 0<=ny<R and visited[ny][nx] == 0 and graph[ny][nx] != "#":
                if graph[ny][nx] == "v":
                    cnt_v +=1
                elif graph[ny][nx] == "k":
                    cnt_k +=1
                q.append((nx,ny))
                visited[ny][nx] = 1
    return cnt_v,cnt_k

total_v = 0
total_k = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != "." and graph[i][j] != "#" and visited[i][j] == 0:
            v,k = bfs(j,i,0,0)
            if v>=k:
                total_v += v
            else:
                total_k += k
print(total_k,total_v)