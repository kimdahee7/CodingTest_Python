dx = [1,0,1,1]
dy = [0,1,1,-1]

graph = [list(map(int,input().split())) for _ in range(19)]
for i in range(19):
  for j in range(19):
    start = graph[i][j]
    if start != 0:
        for k in range(4):
            cnt = 1
            nx = j + dx[k]
            ny = i + dy[k]
            while 0<=nx<19 and 0<=ny<19 and graph[ny][nx] == start:
                cnt +=1
                if cnt == 5:
                    if 0<=nx+dx[k]<19 and 0<=ny+dy[k]<19 and graph[ny+dy[k]][nx+dx[k]] == start:
                        break
                    if 0<=i-dy[k]<19 and 0<=j-dx[k]<19 and graph[i-dy[k]][j-dx[k]] == start:
                        break
                    print(start)
                    print(i+1,j+1)
                    exit()
                nx += dx[k]
                ny += dy[k]
print(0)