N,S = map(int,input().split())
l = list(map(int,input().split()))
answer = []

end = 0
sum = 0
for i in range(N):
    while sum < S and end < N:
        sum += l[end]
        end +=1
    if sum >= S:
        answer.append(end-i)
    sum -= l[i]
if len(answer) == 0:
    print(0)
else:
    print(min(answer))