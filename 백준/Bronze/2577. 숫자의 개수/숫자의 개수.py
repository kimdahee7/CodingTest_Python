def main():
  sum = 1
  L = []
  for i in range(3):
    x = int(input())
    sum = sum*x
  L = list(str(sum))
  for i in range(10):
    print(L.count(str(i)))
   
main()