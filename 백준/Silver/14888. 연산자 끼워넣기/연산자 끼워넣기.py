from itertools import permutations

N = int(input())
A = list(map(int,input().split()))
l = list(map(int,input().split()))
total_cal = []
cal = ["+","-","x","/"]
answer = []

for i in range(4):
    if l[i] != 0:
        for j in range(l[i]):
            total_cal.append(cal[i])

permu = permutations(total_cal,N-1)
for p in permu:
    result = A[0]
    for i in range(1,N):
        if p[i-1] == "+":
            result += A[i]
        elif p[i-1] == "-":
            result -= A[i]
        elif p[i-1] == "x":
            result *= A[i]
        else:
            if result < 0:
                result = -result//A[i]
                result = -result
            else:
                result //= A[i]
    answer.append(result)
answer.sort()
print(answer[-1])
print(answer[0])
