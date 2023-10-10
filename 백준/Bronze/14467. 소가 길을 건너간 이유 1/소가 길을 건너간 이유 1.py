def main(): 
  T = int(input())
  l = {}
  total = 0
  for i in range(T):
    a,b = list(map(int,input().split()))
    if a not in l:
      l[a] = b
    else:
      if l[a] != b:
        l[a] = b
        total +=1
  print(total)
main()