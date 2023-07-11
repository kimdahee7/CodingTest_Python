import sys
input = sys.stdin.readline
def main():
  l = []
  N = int(input())
  for i in range(N):
    M = int(input())
    l.append(M)
  l.sort()
  for j in l:
    print(j)
main()