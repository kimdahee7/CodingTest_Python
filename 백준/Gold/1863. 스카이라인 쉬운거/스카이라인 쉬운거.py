N = int(input())
skyline = []
for i in range(N):
    a,b = map(int,input().split())
    skyline.append(b)
skyline.append(0)

stack = [0]
answer = 0
for i in skyline:
    height = i
    while stack[-1] > i:
        if stack[-1] != height:
            answer +=1
            height = stack[-1]
        stack.pop()
    stack.append(i)

print(answer)