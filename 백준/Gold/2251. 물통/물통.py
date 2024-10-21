import copy
bucket = list(map(int, input().split()))
answer = set()
check = [[[0 for c in range(bucket[2] + 1)] for b in range(bucket[1] + 1)] for a in range(bucket[0] + 1)]

def dfs(a, b, c):
    # 이미 확인한 조합일 경우
    if check[a][b][c] == 1:
        return

    check[a][b][c] = 1
    l = [a, b, c]
    if a == 0:
        answer.add(c)
    for i in range(3):
        for j in range(3):
            if i != j:
                next_l = copy.deepcopy(l)
                # i -> j로 이동
                if next_l[i] > 0 and next_l[j] < bucket[j]:
                    amount = min(next_l[i],bucket[j]-next_l[j])
                    next_l[i] -= amount
                    next_l[j] += amount
                    dfs(next_l[0],next_l[1],next_l[2])

dfs(0, 0, bucket[2])
answer = sorted(answer)
for i in answer:
    print(i,end=" ")