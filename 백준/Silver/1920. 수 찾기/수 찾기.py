import sys
input = sys.stdin.readline
def main():
  N = int(input())
  a = list(map(int,input().split()))
  a.sort()
  M = int(input())
  b = list(map(int,input().split()))
  for i in b:
    print(binary(a,i))

def binary(a,i):
  start = 0 
  end = len(a)-1
  while start <= end:
    mid = (start + end) //2
    if a[mid] == i:
      return "1"
    if a[mid] > i:
      end = mid-1
    else:
      start = mid +1
  return "0"      
main()