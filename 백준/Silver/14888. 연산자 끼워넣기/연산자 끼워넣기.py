N = int(input())
A = list(map(int, input().split()))
l = list(map(int, input().split()))
cal = ["+", "-", "x", "/"]
answer = []


def backtracking(result, l, index):
    if index == N:
        answer.append(result)
        return
    tmp = result
    for i in range(4):
        if l[i] > 0:
            l[i] -= 1
            if i == 0:
                result += A[index]
            elif i == 1:
                result -= A[index]
            elif i == 2:
                result *= A[index]
            else:
                if result < 0:
                    result = -result // A[index]
                    result = -result
                else:
                    result //= A[index]
            backtracking(result, l, index + 1)
            l[i] += 1
            result = tmp

backtracking(A[0], l, 1)
answer.sort()
print(answer[-1])
print(answer[0])
