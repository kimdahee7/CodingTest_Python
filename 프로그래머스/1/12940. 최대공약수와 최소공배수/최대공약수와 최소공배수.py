import math
def solution(n, m):
    answer = []
    a = math.gcd(n,m)
    b = n//a * m//a * a
    return [a,b]