l = ["a","e","o","i","u"]
while True:
  word = input()
  if word == "end":
    break
  a = 0 #모음
  b = 0 #자음
  count = 0
  for i in word:
    if i in l:
      a+=1
      b =0
      if a == 3:
        count +=1
        break
    else:
      b+=1
      a =0
      if b == 3:
        count +=1
        break
  a = 0
  for i in word:
    if i in l:
      a+=1
  if a == 0:
    count +=1
  for i in range(len(word)-1):
    if word[i] == word[i+1] and word[i] != "e" and word[i] != "o":
      count +=1
  if count ==0:
    print("<"+word+"> is acceptable.")
  else:
    print("<"+word+"> is not acceptable.")