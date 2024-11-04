N,M = map(int,input().split())
A = [int(input()) for _ in range(N)]
A.sort()

start = 0
end = 0
answer = A[-1] - A[0]
while 0<=start< N and 0<=end<N:
    result = abs(A[end] - A[start])
    if result >= M:
        answer = min(answer,result)
        start +=1
    elif result == M:
        print(result)
        exit()
    else:
        end +=1

print(answer)