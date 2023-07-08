def main():
  l = []
  k = int(input())
  for i in range(k):
    x = int(input())
    if x !=0:
      l.append(x)
    if x == 0:
      l.pop()
  print(sum(l))
main()