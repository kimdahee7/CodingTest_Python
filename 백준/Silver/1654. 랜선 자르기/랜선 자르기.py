import sys
input = sys.stdin.readline
def main():
  l = []
  k,n = map(int,input().split())
  for _ in range(k):
    cm = int(input())
    l.append(cm)
  start = 1
  end = max(l)
  while start <= end:
    r = 0
    mid = (start+end)//2
    for j in l:
      r += j//mid
    if r>=n:
      start = mid+1
    else:
      end = mid-1
  print(end)
main()