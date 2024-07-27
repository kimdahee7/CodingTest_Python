from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

answer = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            graph[i][j] = -1

# 몇개의 덩어리로 이루어져 있는지 확인
def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<M and 0<=ny<N and graph[ny][nx] != -1 and visited[ny][nx] == False:
                queue.append((nx,ny))
                visited[ny][nx] = True

while True:
    visited = [[False] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != -1 and visited[i][j] == False:
                bfs(j,i,visited)
                count +=1
    if count == 0:
        print(0)
        exit()
    if count >= 2:
        break
    else:
        q = deque()
        for i in range(N):
            for j in range(M):
                if graph[i][j] != -1:
                    q.append((j, i, graph[i][j]))

        while q:
            x, y, k = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == -1:
                    if k ==0:
                        continue
                    else:
                        k -=1
            graph[y][x] = k
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = -1
        answer +=1

print(answer)