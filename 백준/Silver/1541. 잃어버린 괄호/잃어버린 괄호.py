s = input()
split_d = []
split_p = []
result = []
data1 = s.split("-")
for i in data1:
  total = 0
  if "+" in i:
    a = i.split("+")
    for j in a:
      total += int(j)
    split_d.append(total)
  else:
    split_d.append(int(i))

answer1 = split_d[0]
for i in range(1,len(split_d)):
  answer1 -= split_d[i]
result.append(answer1)

data2 = s.split("+")
for i in data2:
  if "-" in i:
    a = i.split("-")
    total = int(a[0])
    for j in range(1,len(a)):
      total -= int(a[j])
    split_p.append(total)
  else:
    split_p.append(int(i))

answer2 = split_p[0]
for i in range(1,len(split_p)):
  answer2 += split_p[i]
result.append(answer2)

print(min(result))