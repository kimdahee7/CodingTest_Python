import sys
input = sys.stdin.readline
def main():
  P = int(input())
  for _ in range(P):
    total = 0
    r = []
    l = list(map(int,input().split()))
    r.append(l[1])
    for i in range(2,len(l)):
      for j in range(i-1):
        if r[j]>l[i]:
          r.insert(j,l[i])
          total += len(r) - j -1
          break
      if l[i] in r:
        continue
      else:
        r.append(l[i])
    print(l[0],total)
main()  