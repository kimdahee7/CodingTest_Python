def main():
  r = 1
  i = 0
  N = int(input())
  while True:
    r += i*6
    if N > r:
      i +=1
      continue
    else:
      print(i+1)
      break   
main()