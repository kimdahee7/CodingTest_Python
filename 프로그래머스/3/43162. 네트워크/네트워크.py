def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    visited = [False] * (n)
    for i in range(n):
        if visited[i] == False:
            dfs(graph,i,visited)
            answer+=1
    return answer

def dfs (graph, n, visited):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)
    