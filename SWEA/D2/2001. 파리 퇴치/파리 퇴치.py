T = int(input())
for t in range(1,T+1):
  N,M = map(int,input().split())
  area = [list(map(int,input().split())) for i in range(N)]
  result = []
  for i in range(N-(M-1)):
    for j in range(N-(M-1)):
      total = 0
      for a in range(i,i+M):
        for b in range(j,j+M):
          total += area[a][b]
      result.append(total)
  print("#"+str(t), max(result))