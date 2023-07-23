import sys
import random 
input = sys.stdin.readline
def main():
  N,M = map(int,input().split())
  l = list(map(int,input().split()))
  max = 0
  for i in range(161700):
    randomlist = random.sample(l,3)
    if sum(randomlist) <= M :
      if max < sum(randomlist):
        max = sum(randomlist)
  print(max)
  
main()