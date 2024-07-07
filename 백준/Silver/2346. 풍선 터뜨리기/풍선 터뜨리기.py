from collections import deque
N = int(input())
l = list(map(int,input().split()))

q = deque()
for i in range(N):
    q.append((i+1,l[i]))

a,b = q.popleft()
answer = [a]
while q:
    if b >0:
        for i in range(b-1):
            q.append(q.popleft())
        a, b = q.popleft()
        answer.append(a)
    else:
        for i in range(abs(b)-1):
            q.appendleft(q.pop())
        a,b = q.pop()
        answer.append(a)
for i in answer:
    print(i, end= " ")