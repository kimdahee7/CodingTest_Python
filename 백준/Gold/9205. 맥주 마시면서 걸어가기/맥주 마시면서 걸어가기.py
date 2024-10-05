from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    graph = []
    for i in range(N+2):
        x, y = map(int,input().split())
        if i == 0:
            start_x = x
            start_y = y
        elif i == N+1:
            end_x = x
            end_y = y
        else: # 편의점 위치 표시
            graph.append((x,y))
    visited = [0] * len(graph)

    q = deque()
    q.append((start_x,start_y))
    c = 0
    while q:
        a,b= q.popleft()
        if abs(end_x-a) + abs(end_y-b) <= 1000:
            print("happy")
            c = 1
            break
        for i in range(len(graph)):
            if visited[i] == 0:
                new_x,new_y = graph[i]
                if abs(new_x - a) + abs(new_y-b) <= 1000:
                    visited[i] = 1
                    q.append((new_x,new_y))
    if c== 0:
        print("sad")