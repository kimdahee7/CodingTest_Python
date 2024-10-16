T = int(input())
for _ in range(T):
    rank = []
    count = 1
    N = int(input())
    for _ in range(N):
        a,b = map(int,input().split())
        rank.append([a,b])
    rank.sort(key=lambda x:(x[0],-x[1]))
    before = rank[0][1]
    for i in range(1,N):
        if rank[i][1] <= before:
            count +=1
            before = rank[i][1]
    print(count)