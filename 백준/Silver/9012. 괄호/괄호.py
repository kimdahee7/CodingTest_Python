def main():
  T = int(input())
  for i in range(T):
    s = input()
    while True:
      if "()" in s:
        s = s.replace("()","")
      else:
        if s == "" :
          print("YES")
          break
        else:
          print("NO")
          break
         
main()