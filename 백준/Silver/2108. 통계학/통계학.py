import sys
input = sys.stdin.readline
from collections import Counter
def main():
  l = []
  N = int(input())
  for i in range(N):
    data = int(input())
    l.append(data)
  l.sort()
  avg = round(sum(l)/N)
  mid = l[N//2]
  m = modefinder(l)
  if len(m) == 1:
    mode = m[0]
  else:
    mode = m[1]
  ran = max(l) - min(l)
  print(avg)
  print(mid)
  print(mode)
  print(ran)
  
def modefinder(list):
    c = Counter(list)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    modes.sort()
    return modes
main()
