import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    first_answer = 1e9
    second_answer = 0

    if K == 1:
        print(1,1)
        continue

    dic = defaultdict(list)
    for i in range(len(W)):
        dic[W[i]].append(i)

    for i in dic:
        if len(dic[i]) >= K:
            for j in range(len(dic[i])-K+1):
                first_answer = min(dic[i][j+K-1]-dic[i][j]+1, first_answer)
                second_answer = max(dic[i][j+K-1]-dic[i][j]+1, second_answer)

    if first_answer == 1e9:
        print(-1)
    else:
        print(first_answer,second_answer)