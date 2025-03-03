N,K = map(int,input().split())
l = list(input())
start = 0
end = 0
answer = 0
for i in range(N):
    if l[i] == "P":
        if i-K <=0:
            start = 0
        else:
            start = i-K
        if i+K >= N-1:
            end = N
        else:
            end = i+K+1
        for j in range(start,end):
            if l[j] == "H":
                l[j] = "D"
                answer +=1
                break
print(answer)
