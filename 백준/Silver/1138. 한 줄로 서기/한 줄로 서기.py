from itertools import permutations
N = int(input())
line = list(map(int,input().split()))
l = [i for i in range(1,N+1)]
p = permutations(l,N)


for i in p:
    dp = [0 for _ in range(N)]
    index = 1
    while index < N:
        count = 0
        for k in range(N):
            if i[k] == index:
                dp[index-1] = count
                break
            elif i[k] > index:
                count +=1
        index += 1
    if dp == line:
        for result in i:
            print(result, end=" ")
        exit()