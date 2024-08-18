from collections import deque
A,B,C = map(int,input().split())
total = A+B+C
visited = [[0 for _ in range(total+1)] for _ in range(total+1)]

q = deque()
q.append((A,B))
visited[A][B] = 1

answer = 0
while q:
    a,b = q.popleft()
    c = total - a - b
    if a == b == c:
        answer = 1
        break
    for x,y in (a,b), (b,c), (a,c):
        if x<y:
            y -= x
            x +=x
        elif x>y:
            x -= y
            y +=y
        else:
            continue
        z = total - x - y
        min_data = min(x,y,z)
        max_data = max(x,y,z)
        if not visited[min_data][max_data]:
            q.append((min_data,max_data))
            visited[min_data][max_data] = 1

print(answer)