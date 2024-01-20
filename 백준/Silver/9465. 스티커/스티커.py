T = int(input())
for _ in range(T):
  n = int(input())
  graph = [list(map(int,input().split())) for _ in range(2)]
  answer = [[0 for _ in range(n)] for _ in range(2)]
  answer[0][0] = graph[0][0]
  answer[1][0] = graph[1][0]

  for j in range(1,n):
    for i in range(2):
      if i == 0:
        answer[i][j] = max(answer[i][j-1],graph[i][j] + answer[1][j-1])
      else:
        answer[i][j] = max(answer[i][j-1],graph[i][j] + answer[0][j-1])
  result = 0
  for i in range(2):
    result = max(result,max(answer[i]))
  print(result)