def main():
  list = []
  for i in range(5):
    x = int(input())
    list.append(x)
  list.sort()
  print(int(sum(list)/5))
  print(list[2])
    
main()