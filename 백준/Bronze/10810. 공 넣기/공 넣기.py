import sys
input = sys.stdin.readline
def main():
  l = []
  N,M = map(int,input().split())
  for _ in range(N):
    l.append(0)
  for _ in range(M):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
      l[x] = k
  for y in l:
    print(y, end=" ")
main()