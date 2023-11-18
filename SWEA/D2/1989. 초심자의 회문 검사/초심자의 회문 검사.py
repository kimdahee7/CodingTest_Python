T = int(input())
for t in range(1,T+1):
  word = input()
  if word == word[::-1]:
    print("#"+str(t), 1)
  else:
    print("#"+str(t), 0)