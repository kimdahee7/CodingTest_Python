N,K = map(int,input().split())
l = list(map(int,input().split()))
dic = {}
for i in l:
    if i not in dic:
        dic[i] = 0

start = 0
end = 0
answer = 1
total = 0
dic[l[start]] +=1
while start < N:
    if end + 1 < N and dic[l[end+1]] + 1 <= K:
        end += 1
        dic[l[end]] += 1
        answer = max(answer,end-start+1)
    else:
        dic[l[start]] -=1
        start +=1

print(answer)