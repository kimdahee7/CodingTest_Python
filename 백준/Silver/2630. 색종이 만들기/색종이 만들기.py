import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

blue = []
white = []

def func(x):
  bl = 0
  w = 0
  for i in range(0,N-x+1,x):
    for j in range(0,N-x+1,x):
      l = []
      for a in range(i,i+x):
        for b in range(j,j+x):
          l.append(paper[a][b])
      if 0 not in l and 2 not in l:
        bl +=1
        for a in range(i,i+x):
          for b in range(j,j+x):
            paper[a][b] = 2
      else:
        if 1 not in l and 2 not in l:
          w +=1
          for a in range(i,i+x):
            for b in range(j,j+x):
              paper[a][b] = 2
  blue.append(bl)
  white.append(w)
       
x = N
while x > 0:
  func(x)
  x = x//2
print(sum(white))
print(sum(blue))