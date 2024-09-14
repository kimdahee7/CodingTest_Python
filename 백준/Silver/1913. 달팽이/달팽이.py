N = int(input())
K = int(input())
map = [[0 for _ in range(N)] for _ in range(N)]

x = N//2
y = N//2
map[y][x] = 1
for i in range(1, N**2):
    #오른쪽 이동 : 아래가 채워져 있고, 오른쪽이 비어있는 경우
    if 0<=x+1<N and 0<=y+1<N and map[y+1][x] != 0 and map[x+1][y] == 0:
        x +=1
        map[y][x] = i + 1
    #위쪽 이동 : 위쪽이 비어있는 경우
    elif 0<=x-1<N and 0<=y-1<N and map[y][x-1] == 0 and map[y-1][x] == 0:
        y -=1
        map[y][x] = i + 1
    #아래쪽 이동 : 왼쪽이 채워져 있고, 아래쪽이 비어있는 경우
    elif 0<=x-1<N and 0<=y+1<N and map[y][x-1] != 0 and map[y+1][x] == 0:
        y +=1
        map[y][x] = i + 1
    #왼쪽 이동 : 위쪽이 채워져 있고, 왼쪽이 비어있는 경우
    elif 0<=x-1<N and 0<=y-1<N and map[y-1][x] != 0 and map[y][x-1] == 0:
        x -=1
        map[y][x] = i + 1

for i in range(N-2,-1,-1):
    map[i][0] = map[i+1][0] + 1

for i in range(N):
   for j in range(N):
       if map[i][j] == K:
           a = i+1
           b = j+1
       print(map[i][j],end=" ")
   print()
print(a,b)