import sys
input = sys.stdin.readline
def main():
  T = int(input())
  for _ in range(T):
    N = int(input())
    l1 = list(map(int,input().split()))
    l1.sort()
    M = int(input())
    l2 = list(map(int,input().split()))
    for i in l2:
      binary(i,l1)

def binary(i,l1):
  r = 0
  start = 0
  end = len(l1)-1
  while start <= end:
    mid = (start+end)//2
    if i < l1[mid]:
      end = mid -1
    elif i > l1[mid]:
      start = mid +1
    else:
      r +=1
      print(1)
      break
  if r == 0:
    print(0)  
main()