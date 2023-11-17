def main():
  T = int(input())
  for t in range(1,T+1):
    n = int(input())
    l = []
    r = []
    for j in range(n):
      if j == 0:
        print("#"+str(t))
        print(1)
      else:
        l.append(1)
        l.insert(0,1)
        for k in l:
          print(k, end=" ")
        print()
        r = l
        l = []
        for i in range(len(r)-1):
          l.append(sum(r[i:i+2]))
main()