import sys
input = sys.stdin.readline
def main():
  l = set()
  N,T = map(str,input().split())
  N = int(N)
  for i in range(N):
    name = input().strip()
    l.add(name)
  c = len(l)
  if T == "Y":
    print(c)
  elif T == "F":
    print(c//2)
  else:
    print(c//3)
main()