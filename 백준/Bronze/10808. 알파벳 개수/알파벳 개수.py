def main():
  x = input()
  for i in range(ord('a'), ord('z')+1):
    print(x.count(chr(i)), end=" ")
   
main()