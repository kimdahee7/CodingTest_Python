N,M = map(int,input().split())
s = [input() for _ in range(N)]

min_data = min(N,M)
answer = 0

for k in range(min_data):
    for i in range(N-k):
        for j in range(M-k):
            if s[i][j] == s[i+k][j+k] == s[i+k][j] == s[i][j+k]:
                answer = max(answer,(k+1)*(k+1))
print(answer)