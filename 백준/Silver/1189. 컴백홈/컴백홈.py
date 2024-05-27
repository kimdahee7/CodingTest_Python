R,C,K = map(int,input().split())
graph = [list(input()) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

global count
count = 0

def dfs(x,y,dist):
    global count
    graph[y][x] = "T"
    if dist == K and x == C-1 and y == 0:
        count +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<=ny<R and graph[ny][nx] == ".":
            graph[ny][nx] = "T"
            dfs(nx,ny,dist+1)
            graph[ny][nx] = "."

dfs(0,R-1,1)
print(count)