N,K = map(int,input().split())
block = list(map(int,input().split()))

answer = 1e9
for i in range(1,1001):
    time = 0
    l = [i + (K*j) for j in range(N)]
    for i in range(N):
        if l[i] != block[i]:
            time +=1
    answer = min(answer,time)
print(answer)