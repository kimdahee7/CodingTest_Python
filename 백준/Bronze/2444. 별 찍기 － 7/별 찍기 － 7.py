def main():
  N = int(input())
  j = N-1
  for i in range(1, N+1):
    print(" "*(N-i)+"*"*(2*i-1))
  for i in range(1, N):
    print(i*" "+(2*j-1)*"*")
    j = j-1
    
main()