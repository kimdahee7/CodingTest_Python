def main():
  N = int(input())
  j = N-1
  for i in range(1, N):
    print("*"*(i)+" "*(2*N-(2*i))+"*"*(i))
  print("*"*(2*N))
  for j in range(1, N):
    print("*"*(N-j)+" "*(2*j)+"*"*(N-j))
    
main()