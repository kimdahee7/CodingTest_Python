import sys
input = sys.stdin.readline
def main():
  N = int(input())
  r = 0
  while N >0:
    if N >=3:
      N-=3
      r+=1
    else:
      N-=1
      r+=1
  if r%2 == 0:
    print("CY")
  else:
    print("SK")
main()