import sys
N,M = map(int,sys.stdin.readline().split())
keyword = {}

for i in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in keyword:
        keyword[word] = 1
answer = N
for _ in range(M):
    l = list(sys.stdin.readline().rstrip().split(","))
    for i in l:
        if i in keyword and keyword[i] == 1:
            keyword[i] -=1
            answer -=1
    print(answer)