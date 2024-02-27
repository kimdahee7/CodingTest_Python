S = list(input())
c0 = S.count("0")//2
c1 = S.count("1")//2
total = 0
for i in S:
  if i == "1":
    S.remove(i)
    total +=1
  if total == c1:
    break
total = 0
S = S[::-1]
for i in S:
  if i == "0":
    S.remove(i)
    total +=1
  if total == c0:
    break
S = S[::-1]
print("".join(S))