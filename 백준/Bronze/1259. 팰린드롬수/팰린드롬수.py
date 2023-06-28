def main():  
  while True:
    s = str(input())
    if s == '0':
      break
    else:
      if s == s[::-1]:
        print("yes")
      else:
        print("no")    
main()