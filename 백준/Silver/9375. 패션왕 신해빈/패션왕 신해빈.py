import sys
input = sys.stdin.readline
def main(): 
  t = int(input())
  for _ in range(t):
    dic = {}
    n = int(input())
    for _ in range(n):
      a,b = map(str,input().split())
      if b in dic:
        dic[b] +=1
      else:
        dic[b] =1
    total = 1
    for i in dic.keys():
      total *= dic[i]+1
    print(total-1)
main()