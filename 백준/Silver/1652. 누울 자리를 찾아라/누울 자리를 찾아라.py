N = int(input())
graph1 = [input() for _ in range(N)]
graph2 = [""] * N
for i in graph1:
    for j in range(N):
        graph2[j] += i[j]
x = 0
y = 0
for i in graph1:
    s = i.split("X")
    for j in s:
        if ".." in j:
            x+=1
for i in graph2:
    s = i.split("X")
    for j in s:
        if ".." in j:
            y+=1

print(x,y)