import random

def main():
  list = []
  total = 0
  for i in range(9):
    x = int(input())
    list.append(x)
  while True:
    randomlist = random.sample(list, 7)
    total = sum(randomlist)
    if total == 100:
      randomlist.sort()
      for i in randomlist:
        print(i)
      break
main()