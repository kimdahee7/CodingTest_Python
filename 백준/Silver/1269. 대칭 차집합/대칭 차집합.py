import sys
input = sys.stdin.readline
def main():
  A,B = map(int,input().split())
  As = list(map(int,input().split()))
  Bs = list(map(int,input().split()))
  As = set(As)
  As2 = As.copy()
  Bs = set(Bs)
  Bs2 = Bs.copy()
  for i in Bs:
    if i in As:
      As2.remove(i)
    Ac = len(As2)
  for j in As:
    if j in Bs:
      Bs2.remove(j)
    Bc = len(Bs2)
  print(Ac+Bc)
main()