import sys
input = sys.stdin.readline

N,M = map(int,input().split())
keyword = {}
for i in range(N):
  word = input().strip()
  keyword[word] = 1
blog = []
answer = N
for _ in range(M):
  blog = list(map(str,input().strip().split(",")))
  for b in blog:
    if b in keyword and keyword[b] != 0:
      keyword[b] -=1
      answer -=1
  print(answer)