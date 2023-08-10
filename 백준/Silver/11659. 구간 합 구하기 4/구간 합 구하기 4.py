import sys
input = sys.stdin.readline
def main():
  r = []
  N,M = map(int,input().split())
  l = list(map(int,input().split()))
  k = 0
  for i in l:
    k +=i
    r.append(k)
  for _ in range(M):
    x,y = map(int,input().split())
    if x == 1:
      print(r[y-1])
    else:
      print(r[y-1]-r[x-2])
main()