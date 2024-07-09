R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
visited = [0] * 30

dx = [1,-1,0,0]
dy = [0,0,1,-1]

global count
count = 0
global answer
answer = 0
def dfs(x,y,dic,graph):
    global count
    global answer
    visited[ord(graph[y][x])-64] = 1
    count +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<=ny<R and visited[ord(graph[ny][nx])-64] == 0:
            dfs(nx,ny,visited,graph)
            visited[ord(graph[ny][nx])-64] = 0
            count -=1
    answer = max(answer,count)
    return answer

print(dfs(0,0,visited,graph))