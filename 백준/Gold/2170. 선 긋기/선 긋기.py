import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append((x, y))

l.sort()
start = l[0][0]
end = l[0][1]
total = 0
for i in range(1, N):
    # 겹쳐있을 경우
    if l[i][0] <= end:
        end = max(end,l[i][1])
    # 시작점이 이전 범위보다 클 경우
    else:
        total += end - start
        start = l[i][0]
        end = l[i][1]
total += end-start
print(total)