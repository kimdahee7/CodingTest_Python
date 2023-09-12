import sys
input = sys.stdin.readline
def main(): 
  T = int(input())
  for _ in range(T):
    N,M = map(int,input().split())
    l = list(map(int,input().split()))
    s = []
    for i in range(N):
      s.append(i)
    total = 0
    while True:
      if l[0] == max(l):
        total +=1
        if s[0] == M:
          print(total)
          break
        else:
          l.pop(0)
          s.pop(0)
      else:
        l.append(l[0])
        s.append(s[0])
        l.pop(0)
        s.pop(0)
  
main()