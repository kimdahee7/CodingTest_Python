N,M = map(int,input().split())
table = [input() for _ in range(N)]
answer = -1
for i in range(N):
  for j in range(M):
    for a in range(-N,N):
      for b in range(-M,M):
        number = ""
        x = i
        y = j
        if a == 0 and b == 0:
          continue
        while 0<=x<N and 0<=y<M:
          number += table[x][y]
          x += a
          y += b
          if int(int(number)**0.5)**2 == int(number):
            answer = max(answer,int(number))

print(answer)
        