N = int(input())
l = [input() for _ in range(N)]
number = ['1','2','3','4','5','6','7','8','9']
l.sort()
n_l = []
for i in l:
    total = 0
    for j in i:
        if j in number:
            total +=int(j)
    n_l.append((total,i))
n_l.sort(key=lambda x:x[0])
answer = []
for i in n_l:
    answer.append(i[1])
answer.sort(key=len)
for i in answer:
    print(i)