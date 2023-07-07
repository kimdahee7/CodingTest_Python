import sys
def main():
  l = []
  N = int(input())
  for i in range(N):
    x = list(map(str, sys.stdin.readline().split()))
    l.append(x)
  for i in range(N):
    l[i][0] = int(l[i][0])
  l.sort(key=lambda x:x[0])
  for a,b in l:
    print(a,b)
main()