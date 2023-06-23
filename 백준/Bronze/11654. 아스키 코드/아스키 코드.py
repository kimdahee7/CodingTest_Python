def main():
  s = input()
  if str(type(s)) == "<class 'int'>":
    print(chr(s))
  else:
    print(ord(s))
  
main()