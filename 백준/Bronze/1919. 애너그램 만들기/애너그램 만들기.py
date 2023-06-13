def main():
  x = str(input())
  listx = list(x)
  removelistx = list(x)
  y = str(input())
  listy = list(y)
  for i in listx:
    if i in listy:
      listy.remove(i)
      removelistx.remove(i)
  print(len(listy)+len(removelistx))
main()