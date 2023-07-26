import sys
input = sys.stdin.readline
def main():
  L = int(input())
  l = list(map(str,input().strip()))
  sum = 0
  for i in range(len(l)):
    if l[i] == "a":
      sum += 1*pow(31,i)
    if l[i] == "b":
      sum += 2*pow(31,i)
    if l[i] == "c":
      sum += 3*pow(31,i)
    if l[i] == "d":
      sum += 4*pow(31,i)
    if l[i] == "e":
      sum += 5*pow(31,i)
    if l[i] == "f":
      sum += 6*pow(31,i)
    if l[i] == "g":
      sum += 7*pow(31,i)
    if l[i] == "h":
      sum += 8*pow(31,i)
    if l[i] == "i":
      sum += 9*pow(31,i)
    if l[i] == "j":
      sum += 10*pow(31,i)
    if l[i] == "k":
      sum += 11*pow(31,i)
    if l[i] == "l":
      sum += 12*pow(31,i)
    if l[i] == "m":
      sum += 13*pow(31,i)
    if l[i] == "n":
      sum += 14*pow(31,i)
    if l[i] == "o":
      sum += 15*pow(31,i)
    if l[i] == "p":
      sum += 16*pow(31,i)
    if l[i] == "q":
      sum += 17*pow(31,i)
    if l[i] == "r":
      sum += 18*pow(31,i)
    if l[i] == "s":
      sum += 19*pow(31,i)
    if l[i] == "t":
      sum += 20*pow(31,i)
    if l[i] == "u":
      sum += 21*pow(31,i)
    if l[i] == "v":
      sum += 22*pow(31,i)
    if l[i] == "w":
      sum += 23*pow(31,i)
    if l[i] == "x":
      sum += 24*pow(31,i)
    if l[i] == "y":
      sum += 25*pow(31,i)
    if l[i] == "z":
      sum += 26*pow(31,i)
  print(sum) 
main()