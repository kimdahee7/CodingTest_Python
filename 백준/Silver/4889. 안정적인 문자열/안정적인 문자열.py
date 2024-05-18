T = 0
while True:
    S = input()
    if "-" in S:
        exit()
    T +=1
    l = []
    for i in S:
        l.append(i)
        if len(l) > 1 and l[-2] == "{" and l[-1] == "}":
            l.pop()
            l.pop()
    count = 0
    while l:
        if l[-1] == l[-2]:
            count +=1
            l.pop()
            l.pop()
        else:
            count +=2
            l.pop()
            l.pop()
    print(str(T)+". "+str(count))