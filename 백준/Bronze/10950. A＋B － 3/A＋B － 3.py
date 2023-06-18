def main():  
  list = []
  T = int(input())
  for i in range(T):
    a,b = map(int,input().split())
    list.append(a+b)
  for i in list:
    print(i)
main()