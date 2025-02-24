N,X = map(int,input().split())
visitor = list(map(int,input().split()))
window = sum(visitor[0:X])
answer = window
dic = {}
dic[answer] = 1
for i in range(X,N):
    window = window + visitor[i] - visitor[i-X]
    if window >= answer:
        answer = window
        if answer not in dic:
            dic[answer] = 1
        else:
            dic[answer] += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(dic[answer])