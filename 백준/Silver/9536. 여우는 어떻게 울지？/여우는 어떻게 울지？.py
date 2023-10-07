import sys
input = sys.stdin.readline
def main():  
  T = int(input())
  r = set()
  for _ in range(T):
    l = list(map(str,input().split()))
    while True:
      s = input().strip()
      if s =="what does the fox say?":
        break
      else:
        sl = list(s.split())
        r.add(sl[2])
    for i in l:
      if i not in r:
        print(i,end=" ")
main()