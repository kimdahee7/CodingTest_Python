N = int(input())
answer = 0
l = [list(map(int,input().split())) for _ in range(N)]

def crash(ind):
    global answer
    #가장 오른쪽에 있는 계란을 치고 난 후
    if ind == N:
        count = 0
        for i in range(N):
            if l[i][0] <= 0:
                count +=1
        answer = max(answer,count)
        return

    #들고 있는 계란이 깨져있는 경우
    if l[ind][0] <= 0:
        crash(ind+1)
        return

    #다른 계란이 다 깨져있는 경우
    check = True
    for i in range(N):
        if i == ind:
            continue
        if l[i][0] > 0:
            check = False
            break
    if check:
        answer = max(answer, N-1)
        return

    #계란을 깰 수 있는 경우
    for i in range(N):
        if i == ind:
            continue
        if l[i][0] <= 0:
            continue
        l[ind][0] -= l[i][1]
        l[i][0] -= l[ind][1]
        crash(ind + 1)
        l[ind][0] += l[i][1]
        l[i][0] += l[ind][1]

crash(0)
print(answer)