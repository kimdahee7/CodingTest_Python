import sys
input = sys.stdin.readline
def main():
  N = int(input())
  l = list(map(int,input().split()))
  l.sort()
  max_data = max(l)
  M = int(input())
  if sum(l) <= M:
    print(max_data)
  else:
    print(binary(l,max_data,M))

def binary(l,max_data,M):
  start = 0
  end = max_data
  r= 0
  while start <= end:
    total = 0
    mid = (start+end) //2 
    for i in l:
      if i <=mid:
        total += i
      else:
        total +=mid
    if total <= M:
      start = mid+1
      r = mid
    else:
      end = mid-1
  return r
main()