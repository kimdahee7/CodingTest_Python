import sys
input = sys.stdin.readline
def main():  
  l = {}
  N = int(input())
  for _ in range(N):
    n = input().strip()
    if n in l:
      l[n] +=1
    else:
      l[n] = 1
  for _ in range(N-1):
    w = input().strip()
    l[w] -=1
  for i in l:
    if l[i] == 1:
      print(i)
main()