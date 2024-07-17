T = int(input())
for _ in range(T):
    L = list(input())
    point = 0
    s1 = [] # 커서 앞
    s2 = [] # 커서 뒤 (거꾸로 정렬)
    for i in L:
        if i == "<":
            if len(s1) != 0:
                s2.append(s1.pop())
        elif i == ">":
            if len(s2) != 0:
                s1.append(s2.pop())
        elif i == "-":
            if len(s1) !=0:
                s1.pop()
        else:
            s1.append(i)
    print("".join(s1) + "".join(s2[::-1]))