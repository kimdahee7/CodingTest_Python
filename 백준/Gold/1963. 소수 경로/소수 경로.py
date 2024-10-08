import math
from collections import deque

prime = [True for _ in range(10000)]
prime[1] = False

for i in range(2,int(math.sqrt(10000))+1):
    if prime[i]:
        j = 2
        while i*j < 10000:
            prime[i*j] = False
            j +=1

T = int(input())
for _ in range(T):
    visited = [0 for _ in range(10000)]
    a,b = map(int,input().split())
    q = deque()
    q.append((a,0))
    visited[a] = 1
    check = 0
    while q:
        x,cnt = q.popleft()
        strx = str(x)
        if x == b:
            print(cnt)
            check = 1
            break
        else:
            for i in range(4):
                for j in range(10):
                    new_num = int(strx[:i] + str(j) + strx[i+1:])
                    if prime[new_num] and new_num >= 1000 and visited[new_num] == 0:
                        q.append((new_num,cnt+1))
                        visited[new_num] = 1
    if check == 0:
        print("Impossible")