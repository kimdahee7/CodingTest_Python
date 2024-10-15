from itertools import permutations

N = int(input())
W = list(map(int,input().split()))

perm = permutations([i for i in range(1,N-1)],N-2)

#오른쪽 탐색
def right_check(index,visited):
    for i in range(index+1,N):
        if visited[i] == 1:
            continue
        else:
            visited[index] = 1
            return W[i]
#왼쪽 탐색
def left_check(index,visited):
    for i in range(index-1,-1,-1):
        if visited[i] == 1:
            continue
        else:
            visited[index] = 1
            return W[i]

answer = 0
for i in perm:
    visited = [0 for _ in range(N)]
    result = 0
    for j in i:
        result += right_check(j,visited)*left_check(j,visited)
    answer = max(answer,result)
print(answer)

