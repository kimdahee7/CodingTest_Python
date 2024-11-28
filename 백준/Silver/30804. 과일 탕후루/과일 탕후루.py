N = int(input())
S = list(map(int,input().split()))
dic = {}
for i in S:
    if i not in dic:
        dic[i] = 0

start = 0
end = 0
total = 0
answer = 0
while end < N:
    dic[S[end]] +=1
    if dic[S[end]] == 1:
        total +=1

    while total > 2:
        dic[S[start]] -=1
        if dic[S[start]] == 0:
            total -=1
        start +=1
    answer = max(answer,end-start+1)
    end +=1
print(answer)
