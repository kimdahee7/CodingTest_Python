def a(i,j,start,graph):
  for _ in range(4):
    if 0<=j+1<19 and graph[i][j+1] == start:
      j +=1
    else:
      return False
  if 0<=j+1<19 and graph[i][j+1] == start:
    return False
  if 0<=j-5<19 and graph[i][j-5] == start:
    return False
  else:
    return True

def b(i,j,start,graph):
  for _ in range(4):
    if 0<=i+1<19 and graph[i+1][j] == start:
      i +=1
    else:
      return False
  if 0<=i+1<19 and graph[i+1][j] == start:
    return False
  if 0<=i-5<19 and graph[i-5][j] == start:
    return False
  else:
    return True

def c(i,j,start,graph):
  for _ in range(4):
    if 0<=i+1<19 and 0<=j+1<19 and graph[i+1][j+1] == start:
      j +=1
      i +=1
    else:
      return False
  if 0<=i+1<19 and 0<=j+1<19 and graph[i+1][j+1] == start:
    return False
  if 0<=i-5<19 and 0<=j-5<19 and graph[i-5][j-5] == start:
    return False
  else:
    return True

def d(i,j,start,graph):
  for _ in range(4):
    if 0<=i-1<19 and 0<=j+1<19 and graph[i-1][j+1] == start:
      j +=1
      i -=1
    else:
      return False
  if 0<=i-1<19 and 0<=j+1<19 and graph[i-1][j+1] == start:
    return False
  if 0<=i+5<19 and 0<=j-5<19 and graph[i+5][j-5] == start:
    return False
  else:
    return True

graph = [list(map(int,input().split())) for _ in range(19)]
for i in range(19):
  for j in range(19):
    start = graph[i][j]
    if start != 0:
      if a(i,j,start,graph) or b(i,j,start,graph) or c(i,j,start,graph) or d(i,j,start,graph):
        print(start)
        print(i+1,j+1)
        exit()
print(0)