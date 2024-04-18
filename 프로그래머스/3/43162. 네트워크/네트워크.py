from collections import deque
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * (n)
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    for i in range(n):
        if visited[i] == False:
            bfs(i,visited,graph)
            answer +=1
    return answer

def bfs(n,visited,graph):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True