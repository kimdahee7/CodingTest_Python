from collections import deque
def solution(maps):
    answer = 0
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                s_x = j
                s_y = i
            if maps[i][j] == "L":
                l_x = j
                l_y = i
            if maps[i][j] == "E":
                e_x = j
                e_y = i
    dist = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
    bfs(s_x,s_y,maps,dist)
    answer += dist[l_y][l_x]
    dist = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
    bfs(l_x,l_y,maps,dist)
    answer += dist[e_y][e_x]
    if answer > INF:
        answer = -1
    return answer


dx = [0,0,1,-1]
dy = [1,-1,0,0]

INF = 1e9

def bfs(x,y,maps,dist):
    q = deque()
    q.append((x,y))
    dist[y][x] = 0 
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps) and maps[ny][nx] != "X":
                if dist[ny][nx] > dist[b][a] + 1:
                    dist[ny][nx] = dist[b][a] + 1
                    q.append((nx,ny))
    