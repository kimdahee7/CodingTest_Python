def main():
  l = []
  N = int(input())
  sum = 1
  result = 0
  for i in range(1,N+1):
    sum *=i
  l = list(str(sum))
  for j in l[::-1]:
    if j == '0':
      result +=1
    else:
      break
  print(result)
main()