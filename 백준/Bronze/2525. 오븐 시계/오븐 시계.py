import sys
input = sys.stdin.readline
def main():
  A,B = map(int,input().split())
  C = int(input())
  r = B + C
  if r <60:
    print(A,r, end=" ")
  else:
    A = A+r//60
    B = r%60
    if A >= 24:
      print(A-24,B, end=" ")
    else:
      print(A,B, end=" ")
main()