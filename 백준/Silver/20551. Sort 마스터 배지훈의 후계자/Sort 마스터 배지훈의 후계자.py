N,M = map(int,input().split())
A = [int(input()) for _ in range(N)]
A.sort()
for i in range(M):
    D = int(input())
    start = 0
    end = len(A) - 1
    answer = 1e9
    while start <= end:
        mid = (start + end) //2
        if A[mid] == D:
            answer = min(answer,mid)
            end = mid - 1
        elif A[mid] > D:
            end = mid -1
        else:
            start = mid +1
    if answer == 1e9:
        print(-1)
    else:
        print(answer)