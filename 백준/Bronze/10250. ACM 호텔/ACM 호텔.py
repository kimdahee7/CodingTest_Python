def main():  
  T = int(input())
  for i in range(T):
    H,W,N = map(int,input().split())
    if N % H == 0:
      y = H *100
      x = N // H 
      print(y+x)
    elif W == 1:
      print(N*100 +1)
    elif N % H != 0 and W !=1:
      y = N % H *100
      x = N // H +1
      print(y+x)
main()