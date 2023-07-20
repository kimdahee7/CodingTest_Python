import sys
input = sys.stdin.readline
from collections import Counter
def main():
  N = int(input())
  NL = list(map(int,input().split()))
  M = int(input())
  ML = list(map(int,input().split()))
  cnt = Counter(NL)
  for i in ML:
    if i in cnt:
      print(cnt[i], end=" ")
    else:
      print("0", end=" ")
main()