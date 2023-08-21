import sys
input = sys.stdin.readline
def main():
  l = []
  num = []
  r = []
  n, k = map(int,input().split())
  for _ in range(n):
    s = list(map(int,input().split()))
    l.append(s)
  l.sort(key = lambda l:l[3], reverse=True)
  l.sort(key = lambda l:l[2], reverse=True)
  l.sort(key = lambda l:l[1], reverse=True)
  for i in l:
    num.append(i[0])
    i.remove(i[0])
  pre = l[0]
  rate = 1
  for j in l:
    if j == pre:
      r.append(rate)
    else:
      rate +=1
      pre = j
      r.append(rate)
  f = num.index(k)
  print(r[f])
main()