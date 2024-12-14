N,M = map(int,input().split())
l = list(map(int,input().split()))
l.sort()

answer = set()
a = []
check = [0] * N
def backtracking():
    if len(a) == M:
        answer.add(tuple(a))
        return
    for i in range(N):
        if check[i] == 0:
            a.append(l[i])
            check[i] = 1
            backtracking()
            a.pop()
            check[i] = 0

backtracking()
answer = sorted(answer)
for i in answer:
    for j in i:
        print(j,end=" ")
    print()