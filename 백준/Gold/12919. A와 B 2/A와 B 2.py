S = input()
T = list(input())

def check(list):
    if "".join(list) == S:
        print(1)
        exit()
    else:
        if len(list) != 0 and list[-1] == "A":
            check(list[0:len(list)-1])
        if len(list) != 0 and list[0] == "B":
            check(list[::-1][0:len(list)-1])

check(T)
print(0)