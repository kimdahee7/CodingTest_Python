N,M = map(int,input().split())
shop = int(input())
# 1 북 - 2 남 - 3 서 - 4 동
l = []
for _ in range(shop):
    x,y = map(int,input().split())
    l.append((x,y))

start_x,start_y = map(int,input().split())

dist = 0
for i in l:
    x,y = i[0],i[1]
    # 동근이가 북쪽에 있을 경우
    if start_x == 1:
        if x == 1:
            dist += abs(y-start_y)
        elif x == 2:
            dist += min(y+start_y+M,(N-y)+(N-start_y)+M)
        elif x == 3:
            dist += start_y + y
        else:
            dist += (N-start_y) + y
    # 남쪽에 있을 경우
    elif start_x == 2:
        if x == 1:
            dist += min(start_y+y+M,(N-y)+(N-start_y)+M)
        elif x == 2:
            dist += abs(y-start_y)
        elif x == 3:
            dist += start_y + (M-y)
        else:
            dist += (N-start_y) + (M-y)
    # 서쪽에 있을 경우
    elif start_x == 3:
        if x == 1:
            dist += start_y + y
        elif x == 2:
            dist += (M-start_y) + y
        elif x == 3:
            dist += abs(y-start_y)
        else:
            dist += min(N+start_y+y,N+(M-start_y)+(M-y))
    # 동쪽에 있을 경우
    else:
        if x == 1:
            dist += start_y + (N-y)
        elif x == 2:
            dist += (M-start_y) + (N-y)
        elif x == 3:
            dist += min(N+start_y+y,N+(M-start_y)+(M-y))
        else:
            dist += abs(y-start_y)
print(dist)