from collections import deque
M,N = map(int,input().split())
graph = [list(input()) for _ in range(M)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    graph[y][x] = "2"
    while q:
        b,a = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[ny][nx] == "0":
                graph[ny][nx] = "2"
                q.append((ny,nx))

for i in range(N):
    if graph[0][i] == "0":
        bfs(0,i)

if "2" in graph[M-1]:
    print("YES")
else:
    print("NO")