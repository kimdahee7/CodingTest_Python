K = int(input())
# 1-동쪽, 2-서쪽, 3-남쪽, 4-북쪽
l1 = []
l2 = []
total = []
for i in range(6):
    a,b = map(int,input().split())
    if a == 1 or a == 2:
        l1.append(b)
        total.append(b)
    else:
        l2.append(b)
        total.append(b)
# 총 가로 길이
max_width = max(l1)
# 총 세로 길이
max_hight = max(l2)

maxhidx = total.index(max_hight)
maxwidx = total.index(max_width)

empty = abs(total[maxhidx-1] - total[(maxhidx-5 if maxhidx == 5 else maxhidx +1)]) * abs(total[maxwidx-1] - total[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])

# 총 넓이
total_area = max_hight * max_width - empty
print(total_area*K)
