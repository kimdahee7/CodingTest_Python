def main():    
  sum = 0
  x = list(map(int,input().split()))
  for i in x:
    sum += i*i
  print(sum%10)
main()