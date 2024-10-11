from itertools import permutations
import copy

N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
l = []
for _ in range(K):
    r,c,s = map(int,input().split())
    l.append((r,c,s))

permu = permutations([i for i in range(K)],K)
answer = 1e9

for i in permu:
    new_a = copy.deepcopy(A)
    for j in i:
        r,c,s = l[j]
        for k in range(s,0,-1):
            left_temp = new_a[r+k-2][c+k-1:c+k]
            right_temp = new_a[r-k][c-k-1:c-k]
            # 아래쪽
            for d in range(r+k-2, r-k-1,-1):
                new_a[d][c+k-1] = new_a[d-1][c+k-1]
            # 윗쪽
            for u in range(r - k, r + k - 1):
                new_a[u][c-k-1] = new_a[u+1][c-k-1]
            # 오른쪽
            new_a[r-k-1][c-k-1:c+k] = right_temp + new_a[r-k-1][c-k-1:c+k-1]
            # 왼쪽
            new_a[r+k-1][c-k-1:c+k] = new_a[r+k-1][c-k:c+k] + left_temp
    for i in range(N):
        answer = min(answer,sum(new_a[i]))
print(answer)