import sys
input = sys.stdin.readline
def main():
  r = []
  answer = []
  N,M = map(int,input().split())
  for _ in range(N):
    s = input().strip()
    r.append(s)
  
  for i in range(N-7):
    for j in range(M-7):
      start_b = 0
      start_w = 0
      for k in range(i,i+8):
        for l in range(j,j+8):
          if (k+l)%2 == 0:
            if r[k][l] != "B":
              start_b +=1
            else:
              start_w +=1
          else:
            if r[k][l] != "W":
              start_b +=1
            else:
              start_w +=1
      answer.append(start_b)
      answer.append(start_w)
  print(min(answer))
                 
main()