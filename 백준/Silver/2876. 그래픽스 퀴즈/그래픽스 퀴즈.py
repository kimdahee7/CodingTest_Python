N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
visited = [[1 for _ in range(2)] for _ in range(N)]

for i in range(N-1):
  for j in range(2):
    if table[i][j] == table[i+1][0] and visited[i+1][0] == 1:
      visited[i+1][0] = visited[i][j] +1
    elif table[i][j] == table[i+1][1] and visited[i+1][1] == 1:
      visited[i+1][1] = visited[i][j] +1

max_data = -1
for i in visited:
  max_data = max(max_data, max(i))

answer = []
for i in range(N):
  for j in range(2):
    if visited[i][j] == max_data:
      answer.append(table[i][j])
print(max_data, min(answer))