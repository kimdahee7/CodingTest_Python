import sys
input = sys.stdin.readline
def main():
  l = []
  A,B = map(str,input().split())
  if A in B:
    print(0)
  else:
    l = []
    al = len(A)
    s = 0
    while True:
      total = 0
      Bc = B[s:s+al]
      if s+al > len(B):
        break
      else:
        for i in range(al):
          if A[i] != Bc[i]:
            total +=1
        l.append(total)
        s +=1
    print(min(l))
main()