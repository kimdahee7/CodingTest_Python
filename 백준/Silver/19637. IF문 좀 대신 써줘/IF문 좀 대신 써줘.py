import sys
input = sys.stdin.readline
N,M = map(int,input().split())
level = []
score = []
for _ in range(N):
  a,b = map(str,input().split())
  level.append(a)
  score.append(int(b))
  
for _ in range(M):
  s = int(input())
  start = 0
  end = N-1
  answer = ""
  while start <= end:
    mid = (start+end)//2
    if score[mid] >= s:
      answer = level[mid]
      end = mid - 1
    else:
      start = mid + 1
  print(answer)