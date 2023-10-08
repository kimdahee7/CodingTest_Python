import sys
input = sys.stdin.readline
def main(): 
  l = []
  r = []
  N = int(input())
  top = list(map(int,input().split()))
  for i in range(N):
    while l:
      if top[i] < l[-1][1]:
        r.append(l[-1][0]+1)
        break
      else:
        l.pop()
    if not l:
      r.append(0)
    l.append([i,top[i]])
  print(" ".join(map(str, r)))
main()