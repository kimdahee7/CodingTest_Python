import sys
import math
input = sys.stdin.readline
def main():
  M,N = map(int,input().split())
  for i in range(M,N+1):
    f(i)
  
def f(i):
  if i == 1:
    return 0
  for j in range(2,int(math.sqrt(i))+1):
    if i%j == 0:
      return 0
  print(i)
     
main()