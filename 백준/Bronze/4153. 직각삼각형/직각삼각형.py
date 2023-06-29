def main():  
  while True:
    a,b,c = map(int,input().split())
    if a == 0 and b ==0 and c ==0:
      break
    else:
      if a >b and a>c:
        if a**2 == b**2 + c**2:
          print("right")
        else:
          print("wrong")
      elif b>c and b>a:
        if b**2 == a**2 + c**2:
          print("right")
        else:
          print("wrong")
      else:
        if c**2 == a**2 + b**2:
          print("right")
        else:
          print("wrong")
main()