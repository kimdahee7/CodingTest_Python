N = int(input())
l = [int(input()) for _ in range(N)]
l.sort(reverse=True)
answer = 0
for i in range(N):
    answer = max(answer,(i+1)*l[i])
print(answer)