import sys
input = sys.stdin.readline
def main():
  l = []
  r = []
  n = int(input())
  if n == 0:
    print(0)
  else:
    for _ in range(n):
      o = int(input())
      l.append(o)
    l.sort()
    level = int(n*0.15 + 0.5)
    for i in range(level,n-level):
      r.append(l[i])
    print(int(sum(r)/len(r)+0.5))
main()