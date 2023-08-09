import sys
input = sys.stdin.readline
def main():
  l = [] 
  l = [i for i in range(1,15)]
  T = int(input())
  for _ in range(T):
    k = int(input())
    n = int(input())
    if n == 1:
      print(1)
    else:
      t = 0
      if k == 1:
        for j in range(0,n):
          t += l[j]
        print(t)
      else:
        r = [i for i in range(1,15)]
        for z in range(k-1):
          data = 0
          for x in range(0,n):
            data += r[x]
            r[x] = data
        t = 0
        for y in range(0,n):
          t +=r[y]
        print(t)
main()