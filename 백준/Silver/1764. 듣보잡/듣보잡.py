import sys
input = sys.stdin.readline
def main():
  h = set()
  s = set()
  r = []
  N,M = map(int,input().split())
  for _ in range(N):
    x = input().strip()
    h.add(x)
  for _ in range(M):
    y = input().strip()
    s.add(y)
  for i in h:
    if i in s:
      r.append(i)
  print(len(r))
  r.sort()
  for j in r:
    print(j)
main()