def main(): 
  T = int(input())
  for k in range(1,T+1):
    total = 0
    c = int(input())
    for i in range(1,c+1):
      if i%2 ==0:
        total -= i 
      else:
        total += i
    print("#"+str(k),end=" ")
    print(total)
main()