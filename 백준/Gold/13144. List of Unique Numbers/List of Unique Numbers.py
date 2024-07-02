N = int(input())
l = list(map(int,input().split()))

start = 0
end = 0
answer = 0

dic = {}
for i in l:
    dic[i] = 0

while start < N and end < N:
    if dic[l[end]] + 1 == 1:
        answer += end - start + 1
        dic[l[end]] +=1
        end +=1
    else:
        dic[l[start]] -=1
        start +=1
print(answer)