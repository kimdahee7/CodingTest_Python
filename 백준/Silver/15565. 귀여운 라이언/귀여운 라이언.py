N,K = map(int,input().split())
l = list(map(int,input().split()))

start = 0
end = 0
answer = 1e9
total = 0
if l[start] == 1:
    total +=1
while end < N:
    if total == K:
        answer = min(answer,end-start+1)
        if l[start] == 1:
            total -=1
        start += 1
    else:
        end +=1
        if end < N and l[end] == 1:
            total +=1

if answer == 1e9:
    print(-1)
else:
    print(answer)