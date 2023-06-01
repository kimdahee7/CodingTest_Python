def main():
  N = int(input())
  for i in range(N):
    for j in range(N):
      print("*", end="")
    N = N-1
    print("")

main()