import sys
input = sys.stdin.readline
def main():
  l = {}
  N,M = map(int,input().split())
  for _ in range(N):
    s,p = map(str,input().split())
    l[s] = p
  for _ in range(M):
    search = input().strip()
    print(l[search])
main()