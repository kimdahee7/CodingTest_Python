def main():
  N = int(input())
  j = N
  for i in range(0, N):
    print(i*" "+(2*j-1)*"*")
    j = j-1

main()