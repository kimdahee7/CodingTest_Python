def main():
  N = int(input())
  for i in range(0, N):
    print(" "*(i)+"*"*(2*N-1-(i*2)))
  for i in range(0, N-1):
    print(" "*(N-2-i)+"*"*(2*i+3))
    
main()