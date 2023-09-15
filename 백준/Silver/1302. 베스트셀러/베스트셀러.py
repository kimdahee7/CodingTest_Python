import sys
input = sys.stdin.readline
from collections import Counter
def main():
  l = []
  N = int(input())
  for _ in range(N):
    s = input().strip()
    l.append(s)
  c = dict(Counter(l))
  max_data = max(c.values())
  result = []
  for k, v in c.items():
    if v == max_data:
      result.append(k)
  result.sort()
  print(result[0])
main()