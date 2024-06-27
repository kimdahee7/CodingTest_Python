N,M = map(int,input().split())
l = list(map(int,input().split()))

l.sort()
start = 0
end = N-1

answer = 0
while start<end:
    sum = l[start] + l[end]
    if sum < M:
        start +=1
    else:
        answer +=1
        start +=1
        end -=1
print(answer)
