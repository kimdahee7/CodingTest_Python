from itertools import combinations
while True:
    S = list(map(int, input().split()))
    k = S[0]
    if k == 0:
        exit()
    S = S[1::]
    S.sort()
    combi = combinations(S,6)
    for c in combi:
        for i in c:
            print(i,end=" ")
        print()
    print()