N = int(input())
out_l = []
dic = {}
for i in range(N):
    car = input()
    if car not in dic:
        dic[car] = i
for i in range(N):
    car = input()
    out_l.append(dic[car])

cnt = 0
for i in range(N):
    now = out_l[i]
    for after in range(i+1,N):
        if now > out_l[after]:
            cnt += 1
            break
print(cnt)