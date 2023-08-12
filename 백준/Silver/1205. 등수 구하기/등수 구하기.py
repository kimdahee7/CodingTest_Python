import sys
input = sys.stdin.readline
def main():
  rank = 1
  N,S,P = map(int,input().split())
  if N == 0:
    print(1)
  else:
    r = list(map(int,input().split()))
    for i in r:
      if i > S:
        rank+=1
    if N == P:
      if min(r) >= S:
        print(-1)
      else:
        print(rank)
    else:
      print(rank)
main()