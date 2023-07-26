import sys
input = sys.stdin.readline
def main():
  L = int(input())
  l = list(map(str,input().strip()))
  print(hashing(l))

def hashing(l):
  sum = 0
  for i in range(len(l)):
    if l[i] == "a":
      sum += 1*(31**i)
    if l[i] == "b":
      sum += 2*(31**i)
    if l[i] == "c":
      sum += 3*(31**i)
    if l[i] == "d":
      sum += 4*(31**i)
    if l[i] == "e":
      sum += 5*(31**i)
    if l[i] == "f":
      sum += 6*(31**i)
    if l[i] == "g":
      sum += 7*(31**i)
    if l[i] == "h":
      sum += 8*(31**i)
    if l[i] == "i":
      sum += 9*(31**i)
    if l[i] == "j":
      sum += 10*(31**i)
    if l[i] == "k":
      sum += 11*(31**i)
    if l[i] == "l":
      sum += 12*(31**i)
    if l[i] == "m":
      sum += 13*(31**i)
    if l[i] == "n":
      sum += 14*(31**i)
    if l[i] == "o":
      sum += 15*(31**i)
    if l[i] == "p":
      sum += 16*(31**i)
    if l[i] == "q":
      sum += 17*(31**i)
    if l[i] == "r":
      sum += 18*(31**i)
    if l[i] == "s":
      sum += 19*(31**i)
    if l[i] == "t":
      sum += 20*(31**i)
    if l[i] == "u":
      sum += 21*(31**i)
    if l[i] == "v":
      sum += 22*(31**i)
    if l[i] == "w":
      sum += 23*(31**i)
    if l[i] == "x":
      sum += 24*(31**i)
    if l[i] == "y":
      sum += 25*(31**i)
    if l[i] == "z":
      sum += 26*(31**i)
  return sum 
main()