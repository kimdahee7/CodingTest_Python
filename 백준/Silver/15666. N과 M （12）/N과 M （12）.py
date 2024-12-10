from itertools import product
N,M = map(int,input().split())
l = list(map(int,input().split()))
l.sort()

pro = product(l,repeat=M)
answer = set()
for i in pro:
    i = list(i)
    i.sort()
    answer.add(tuple(i))
answer = sorted(answer)
for i in answer:
    for j in i:
        print(j,end=" ")
    print()