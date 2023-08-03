import sys
input = sys.stdin.readline
def main():
  l = []
  N,M = map(int,input().split())
  for i in range(1,N+1):
    l.append(i)
  for _ in range(M):
    s,e = map(int,input().split())
    r = e
    temp = 0
    end = s+(e-s)//2
    for j in range(s-1,e):
      if j == end:
        break
      else: 
        temp = l[j]
        l[j] = l[r-1]
        l[r-1] = temp  
        r -=1
  for t in l:
    print(t, end=" ")
              
main()