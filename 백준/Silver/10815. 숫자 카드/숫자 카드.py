import sys
input = sys.stdin.readline
def main():
  N = int(input())
  NL = list(map(int,input().split()))
  NL = set(NL)
  M = int(input())
  ML = list(map(int,input().split()))
  for i in ML:
    if i in NL:
      print("1",end=" ")
    else:
      print("0",end=" ")
main()