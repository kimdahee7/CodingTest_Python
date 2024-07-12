from collections import deque

N, M = map(int, input().split())
l = list(map(int, input().split()))

q = deque()
for i in range(1, N + 1):
    q.append(i)

answer = 0
for i in l:
    while True:
        if i == q[0]:
            q.popleft()
            break
        mid = len(q)//2
        if q.index(i) <= mid:
            q.append(q.popleft())
            answer += 1
        else:
            q.appendleft(q.pop())
            answer += 1
print(answer)