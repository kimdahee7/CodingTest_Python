def main():
  score = 0
  total = 0
  for i in range(20):
    x,y,z = map(str,input().split())
    if z != "P":
      if z == "A+":
        total += (float(y)*4.5)
        score +=float(y)
      if z == "A0":
        total += (float(y)*4.0)
        score +=float(y)
      if z == "B+":
        total += (float(y)*3.5)
        score +=float(y)
      if z == "B0":
        total += (float(y)*3.0)
        score +=float(y)
      if z == "C+":
        total += (float(y)*2.5)
        score +=float(y)
      if z == "C0":
        total += (float(y)*2.0)
        score +=float(y)
      if z == "D+":
        total += (float(y)*1.5)
        score +=float(y)
      if z == "D0":
        total += (float(y)*1.0)
        score +=float(y)
      if z == "F":
        total += (float(y)*0.0)
        score +=float(y)
  print('{:.6f}'.format(total / score))
    
main()