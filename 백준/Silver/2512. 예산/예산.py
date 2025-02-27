N = int(input())
N_list = list(map(int,input().split()))
M = int(input())

N_list.sort()
start = 0
end = N_list[-1]
result = 0
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in N_list:
        if i <= mid:
            total += i
        else:
            total += mid
    if total > M:
        end -=1
    elif total < M:
        if result < total:
            result = total
            answer = mid
        start +=1
    else:
        print(mid)
        exit()
print(answer)