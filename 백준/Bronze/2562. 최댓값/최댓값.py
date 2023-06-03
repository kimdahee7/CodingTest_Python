def main():
  list = []
  for i in range(9):
    N = int(input())
    list.append(N)
  print(max(list))
  print((list.index(max(list))+1))
    
main()