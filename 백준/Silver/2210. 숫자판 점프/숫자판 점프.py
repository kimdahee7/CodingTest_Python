graph = [list(map(int,input().split())) for _ in range(5)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = set()

def dfs(x,y,number):
    number += str(graph[y][x])
    if len(number) == 6:
        answer.add(number)
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,number)


for y in range(5):
    for x in range(5):
        num = dfs(x,y,"")

print(len(answer))
