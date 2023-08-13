import sys
input = sys.stdin.readline
def main(): 
  while True:
    l = []
    a,b,c = list(map(int,input().split()))
    l.append(a)
    l.append(b)
    l.append(c)
    m = max(l)
    r = l.remove(m)
    if a == b == c == 0:
      break
    else:
      if m < sum(l):
        if a == b == c:
          print("Equilateral")
        elif a ==b or b == c or a ==c:
          print("Isosceles")
        elif a != b and a!= c and b !=c:
          print("Scalene")
      else:
        print("Invalid")
main()