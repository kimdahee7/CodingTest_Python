N = int(input())
cookie = [list(input()) for _ in range(N)]

x = 0
y = 0
c = 0
# 심장 위치 구하기
for i in range(N):
    for j in range(N):
        if cookie[i][j] == "*":
            x = j
            y = i + 1
            c += 1
            break
    if c != 0:
        break
print(y + 1, x + 1)

# 왼쪽 팔 길이
a = 0
for i in range(x):
    if cookie[y][i] == "*":
        a += 1

# 오른쪽 팔 길이
b = 0
for i in range(x + 1, N):
    if cookie[y][i] == "*":
        b += 1

# 허리 길이
c = 0
for i in range(y+1,N):
    if cookie[i][x] == "*":
        c +=1

# 왼쪽 다리의 길이
d = 0
for i in range(y+1,N):
    if cookie[i][x-1] == "*":
        d +=1

# 오른쪽 다리의 길이
e = 0
for i in range(y+1,N):
    if cookie[i][x+1] == "*":
        e +=1

print(a,b,c,d,e)