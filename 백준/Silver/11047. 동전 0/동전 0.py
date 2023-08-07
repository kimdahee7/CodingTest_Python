import sys
input = sys.stdin.readline
def main():
  l = []
  t = 0
  N,K = map(int,input().split())
  for _ in range(N):
    x = int(input())
    l.append(x)
  l.sort(reverse=True)
  for i in l:
    if K >= i:
      t +=K//i
      K = K%i
  print(t)
main()