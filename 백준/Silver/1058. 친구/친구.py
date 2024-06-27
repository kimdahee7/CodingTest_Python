N = int(input())
friend = [list(input()) for _ in range(N)]
graph = [[0 for _ in range(N)] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if friend[i][j] == "Y" or (friend[i][k] == "Y" and friend[k][j] =="Y"):
                graph[i][j] = 1
answer = 0
for i in graph:
    answer = max(answer,sum(i))
print(answer)