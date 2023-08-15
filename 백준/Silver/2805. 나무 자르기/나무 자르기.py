import sys
input = sys.stdin.readline
def main():
  N,M = map(int,input().split())
  l = list(map(int,input().split()))
  start = 0
  end = max(l)
  while start <= end:
    r = 0
    mid = (start+end)//2
    for i in l:
      if i > mid:
        r += i-mid
    if r >= M:
      start = mid+1
    else:
      end = mid-1
  print(end)
main()