import sys
input = sys.stdin.readline
import math
def main():
  A,B = map(int,input().split())
  C,D = map(int,input().split())
  lcm = math.lcm(B,D)
  rA = (lcm//B)*A + (lcm//D)*C
  rB = lcm
  gcd = math.gcd(rA,rB)
  print(rA//gcd, rB//gcd)
main()