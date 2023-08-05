import sys
input = sys.stdin.readline
from string import ascii_uppercase
def main():
  a = {}
  r = ""
  j = 10
  for i in ascii_uppercase:
    a[i] = j
    j +=1
  a = {v:k for k,v in a.items()}
  N,B = map(int,input().split())
  while N != 0:
    if N%B in a:
      r += a[N%B]
      N = N//B
    else:
      r += str(N%B)
      N = N//B
  print(r[::-1])
main()