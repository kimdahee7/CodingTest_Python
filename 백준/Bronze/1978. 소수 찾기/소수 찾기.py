def main():  
  result = 0
  N = int(input())
  x = list(map(int,input().split()))
  for i in x:
    sum = 0
    for j in range(1, i+1):
      if i % j == 0:
        sum +=1
    if sum ==2:
      result +=1
  print(result)
           
main()