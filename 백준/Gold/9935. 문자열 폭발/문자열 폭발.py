word = list(input())
b = input()
n = len(b)
stack = []

for i in word:
    stack.append(i)
    if len(stack) < n:
        continue
    else:
        if "".join(stack[len(stack)-n:len(stack)]) == b:
            for _ in range(n):
                stack.pop()
if len(stack) > 0:
    print("".join(stack))
else:
    print("FRULA")