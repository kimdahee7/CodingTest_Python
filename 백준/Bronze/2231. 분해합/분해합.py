def main():
  N = int(input())
  for i in range(1,N+1):
    if N == i + sum(list(map(int,str(i)))):
      print(i)
      break
    if N == i:
      print("0")
main()