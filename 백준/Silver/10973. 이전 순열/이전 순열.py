N = int(input())
l = list(map(int,input().split()))

for i in range(len(l)-1,0,-1):
    if l[i] < l[i-1]:
        for j in range(len(l)-1,0,-1):
            if l[i-1] > l[j]:
                l[i-1],l[j] = l[j],l[i-1]
                A = sorted(l[i::],reverse=True)
                l = l[:i] + A
                for num in l:
                    print(num,end=" ")
                exit()
print(-1)