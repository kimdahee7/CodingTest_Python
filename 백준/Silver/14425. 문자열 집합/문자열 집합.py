import sys
input = sys.stdin.readline
def main():
  NL = set()
  r = 0
  N,M = map(int,input().split())
  for _ in range(N):
    s = input().strip()
    NL.add(s)
  for _ in range(M):
    data = input().strip()
    if data in NL:
      r +=1
  print(r)
main()