S = input()
stack = []
answer = 0
tmp = 1
for i in range(len(S)):
    if S[i] == "(":
        stack.append("(")
        tmp *=2
    elif S[i] == "[":
        stack.append("[")
        tmp *=3
    elif S[i] == ")":
        if len(stack) == 0 or stack[-1] == "[":
            print(0)
            exit()
        elif S[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if len(stack) == 0 or stack[-1] == "(":
            print(0)
            exit()
        elif S[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if len(stack) !=0:
    print(0)
else:
    print(answer)