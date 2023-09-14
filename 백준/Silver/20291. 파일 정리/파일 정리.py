import sys
input = sys.stdin.readline
from collections import Counter
def main(): 
  l = []
  N = int(input())
  for _ in range(N):
    s = input().strip()
    s = s.split(".")
    l.append(s[1])
  c = dict(Counter(l))
  dic = dict(sorted(c.items()))
  for key, value in dic.items():
    print(key,value)
main()