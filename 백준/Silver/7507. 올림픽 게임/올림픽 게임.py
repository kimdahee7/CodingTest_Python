T = int(input())
for t in range(T):
    N = int(input())
    l = []
    for _ in range(N):
        D,S,E = map(int,input().split())
        l.append((D,S,E))
    l.sort(key=lambda x:(x[0],x[2],x[1]))
    d = l[0][0]
    e = l[0][2]
    answer = 1
    for i in range(1,N):
        # 이전 날짜와 다른 경우
        if l[i][0] != d:
            answer +=1
            e = l[i][2]
            d = l[i][0]
        # 이전 날짜와 같은 경우
        else:
            if e <= l[i][1]:
                answer +=1
                e = l[i][2]
                d = l[i][0]
            else:
                continue
    print("Scenario #"+str(t+1)+":")
    print(answer)
    print()
