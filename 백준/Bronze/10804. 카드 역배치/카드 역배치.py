def main():
  list = []
  for i in range(1,21):
    list.append(i)  

  for i in range(10):
    a, b = map(int, input().split())
    n = b
    x = 0
    for j in range(a-1, b):
      if j <= n-1:
        x = list[j]
        list[j] = list[n-1]
        list[n-1] = x
      n = n-1
  print(*list)
 
main()