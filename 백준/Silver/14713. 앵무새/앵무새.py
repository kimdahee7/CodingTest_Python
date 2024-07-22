N = int(input())
l = []
for _ in range(N):
    tmp = list(input().split())
    l.append(tmp)
L = list(input().split())

for i in L:
    c = 0
    for j in l:
        if len(j) !=0 and i == j[0]:
            c +=1
            j.pop(0)
    if c ==0:
        print("Impossible")
        exit()

for i in l:
    if len(i) !=0:
        print("Impossible")
        exit()
print("Possible")