def main():
  l = []
  while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
      break
    else:
      l.append(a+b)
  for i in l:
    print(i)
main()