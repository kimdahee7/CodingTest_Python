from collections import deque

def solution(land):
    answer = 0
    X = len(land[0])
    Y = len(land)
    pipe = []
    visited = [[0 for i in range(X)] for _ in range(Y)]
    count = 1
    for x in range(X):
        total = 0
        check = set()
        for y in range(Y):
            if land[y][x] == 1 and visited[y][x] == 0:
                result = bfs(x,y,X,Y,count,land,visited)
                total += result
                pipe.append(result)
                check.add(count)
                count +=1
            elif land[y][x] == 1 and visited[y][x] != 0 and visited[y][x] not in check:
                total += pipe[visited[y][x]-1]
                check.add(visited[y][x])
                
        answer = max(answer,total)
    return answer


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,X,Y,count,land,visited):
    cnt = 1
    q = deque()
    q.append((x,y))
    visited[y][x] = count
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0<=nx<X and 0<=ny<Y and visited[ny][nx] == 0 and land[ny][nx] == 1:
                q.append((nx,ny))
                visited[ny][nx] = count
                cnt +=1
    return cnt
                
    
    