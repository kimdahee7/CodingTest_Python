N,K = map(int,input().split())
a = list(map(int,input().split()))
dic = {}
for i in a:
    if i not in dic:
        dic[i] = 0

start = 0
end = 1
tmp = 1
answer = 1
dic[a[0]] = 1
while start <= end < N:
    if (dic[a[end]] + 1) <= K:
        dic[a[end]] +=1
        end +=1
        tmp +=1
    else:
        dic[a[start]] -=1
        start +=1
        tmp -=1
    answer = max(answer,tmp)
print(answer)