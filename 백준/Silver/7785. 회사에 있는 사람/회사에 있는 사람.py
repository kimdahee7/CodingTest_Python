import sys
input = sys.stdin.readline
def main():
  l = set()
  N = int(input())
  for i in range(N):
    A,B = map(str, input().split())
    if B == "enter":
      l.add(A)
    else:
      l.remove(A)
  l = list(l)
  l.sort(reverse=True)
  for j in l:
    print(j)
main()