def main():  
  ns = []
  N = int(input())
  s = list(map(int,input().split()))
  M = max(s)
  for i in s:
    ns.append(i/M*100)
  print(sum(ns)/N)
  
main()