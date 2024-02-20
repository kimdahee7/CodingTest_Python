n,m,r = map(int,input().split())
item = list(map(int,input().split()))
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0
      graph[j][i] = 0

for i in range(r):
  a,b,c = map(int,input().split())
  graph[a][b] = c
  graph[b][a] = c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])
    
answer = []
for i in range(1,len(graph)):
  total = 0
  for j in range(1,len(graph[i])):
    if graph[i][j] <= m:
      total += item[j-1]
  answer.append(total)
print(max(answer))