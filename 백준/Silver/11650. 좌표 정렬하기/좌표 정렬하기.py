import sys
def main():
  l = []
  N = int(input())
  for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    l.append(x)
  l.sort(key=lambda x:x[1])
  l.sort(key=lambda x:x[0])
  for a,b in l:
    print(a,b)
main()