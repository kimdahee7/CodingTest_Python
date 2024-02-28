s = input()
num = 0
idx = 0
while True:
  num +=1
  for i in str(num):
    if i == s[idx]:
      idx +=1
      if idx >= len(s):
        print(num)
        exit()