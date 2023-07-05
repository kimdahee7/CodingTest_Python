import sys
def main():
  l = []
  N = int(input())
  for i in range(N):
    s = str(sys.stdin.readline().strip())
    l.append(s)
  l = list(set(l))
  l.sort()
  l.sort(key = len)
  for i in l:
    print(i)
main()