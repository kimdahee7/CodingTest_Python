N,M = map(int,input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            if i+2 >= N or j+2 >= M:
                continue
            for a in range(i,i+3):
                for b in range(j,j+3):
                    if A[a][b] == "1":
                        A[a][b] = "0"
                    else:
                        A[a][b] = "1"
            answer +=1

if A == B:
    print(answer)
else:
    print(-1)
