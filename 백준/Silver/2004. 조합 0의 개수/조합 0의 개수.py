n,m = map(int,input().split())

def count_two(n):
    count = 0
    divisor = 2
    i = 2
    while divisor <= n:
        count += n // divisor
        divisor = 2**i
        i +=1
    return count

def count_five(n):
    count = 0
    divisor = 5
    i = 2
    while divisor <= n:
        count += n// divisor
        divisor = 5**i
        i +=1
    return count

# 총 2의 개수
a = count_two(n) - count_two(m) - count_two(n-m)
# 총 5의 개수
b = count_five(n) - count_five(m) - count_five(n-m)
print(min(a,b))