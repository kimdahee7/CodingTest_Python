import sys
input = sys.stdin.readline
def main():
  t = 0
  r = 0
  N = int(input())
  l = list(map(int,input().split()))
  l.sort()
  for i in l:
    t += i
    r += t
  print(r)
main()