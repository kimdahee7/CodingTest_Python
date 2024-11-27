N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append((x, y))

l.sort(key=lambda x: (x[0], -x[1]))
start = l[0][0]
end = l[0][1]
total = end - start
for i in range(1, N):
    # 이전 범위에 포함되어 있을 경우
    if start <= l[i][0] and l[i][1] <= end:
        continue
    # 시작점이 이전 범위보다 클 경우
    elif end < l[i][0]:
        total += l[i][1] - l[i][0]
        start = l[i][0]
        end = l[i][1]
    # 범위가 겹쳐있을 경우
    elif start <= l[i][0] and l[i][1] > end:
        total += l[i][1] - end
        end = l[i][1]

print(total)
