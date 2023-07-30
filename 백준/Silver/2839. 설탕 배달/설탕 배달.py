import sys
input = sys.stdin.readline
def main():
  l = []
  s = 0
  N = int(input())
  if N%5 == 0:
    l.append(N//5)
  if N%3 == 0:
    l.append(N//3)
  for i in range(1, N):
    s = N - (3*i)
    if s > 0 :
      if s % 5 == 0:
        l.append(i+(s//5))
    else:
      if N >= 5:
        s = N - (5*i)
        if s > 0:
          if s % 3 == 0:
            l.append(i+(s//3))
  if len(l) == 0:
    print("-1")
  else:
    print(min(l))
    
main()