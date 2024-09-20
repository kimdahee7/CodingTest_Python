a = list(map(int,input()))
b = list(map(int,input()))
c = list(map(int,input()))
d = list(map(int,input()))
# N - 0 / S -1

answer = 0

# 시계방향을 돌릴 경우
def turn_right(x):
    new_list = x[7:] + x[:7]
    return new_list

# 시계반대방향으로 돌릴 경우
def turn_left(x):
    new_list = x[1:] + x[:1]
    return new_list

# 첫번째 톱니는 3번째, 두번째 톱니는 7번째,3번째
# 세번째 톱니는 7번째,3번째, 네번째 톱니는 7번째
K = int(input())
for _ in range(K):
    N,D = map(int,input().split())
    a2 = a[2]
    a6 = a[6]
    b6 = b[6]
    b2 = b[2]
    c2 = c[2]
    c6 = c[6]
    d2 = d[2]
    d6 = d[6]
    # 첫번째 톱니를 돌릴 경우
    if N == 1:
        # 시계 방향으로 돌릴 경우
        if D == 1:
            a = turn_right(a)
            if a2 != b6:
                b = turn_left(b)
                if b2 != c6:
                    c = turn_right(c)
                    if c2 != d6:
                        d = turn_left(d)
        # 반시계 방향으로 돌릴 경우
        else:
            a = turn_left(a)
            if a2 != b6:
                b = turn_right(b)
                if b2 != c6:
                    c = turn_left(c)
                    if c2 != d6:
                        d = turn_right(d)
    # 두번째 톱니를 돌릴 경우
    if N == 2:
        # 시계 방향으로 돌릴 경우
        if D == 1:
            b = turn_right(b)
            if b6 != a2:
                a = turn_left(a)
            if b2 != c6:
                c = turn_left(c)
                if c2 != d6:
                    d = turn_right(d)
        # 반시계 방향으로 돌릴 경우
        else:
            b = turn_left(b)
            if b6 != a2:
                a = turn_right(a)
            if b2 != c6:
                c = turn_right(c)
                if c2 != d6:
                    d = turn_left(d)
    # 세번째 톱니를 돌릴 경우
    if N == 3:
        # 시계 방향으로 돌릴 경우
        if D == 1:
            c = turn_right(c)
            if c2 != d6:
                d = turn_left(d)
            if c6 != b2:
                b = turn_left(b)
                if b6 != a2:
                    a = turn_right(a)
        # 반시계 방향으로 돌릴 경우
        else:
            c = turn_left(c)
            if c2 != d6:
                d = turn_right(d)
            if c6 != b2:
                b = turn_right(b)
                if b6 != a2:
                    a = turn_left(a)
    # 네번째 톱니를 돌릴 경우
    if N == 4:
        # 시계 방향으로 돌릴 경우
        if D == 1:
            d = turn_right(d)
            if d6 != c2:
                c = turn_left(c)
                if c6 != b2:
                    b = turn_right(b)
                    if b6 != a2:
                        a = turn_left(a)
        # 반시계 방향으로 돌릴 경우
        else:
            d = turn_left(d)
            if d6 != c2:
                c = turn_right(c)
                if c6 != b2:
                    b = turn_left(b)
                    if b6 != a2:
                        a = turn_right(a)
if a[0] == 1:
    answer +=1
if b[0] == 1:
    answer +=2
if c[0] == 1:
    answer +=4
if d[0] == 1:
    answer +=8
print(answer)
