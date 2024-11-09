T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int,input().split()))

    L.sort()
    answer = L[1] - L[0]
    tmp1 = L[0]
    tmp2 = L[1]
    for i in range(len(L)):
        if i % 2 ==0:
            answer = max(answer,L[i]-tmp1)
            tmp1 = L[i]
        else:
            answer = max(answer,L[i]-tmp2)
            tmp2 = L[i]

    print(answer)
