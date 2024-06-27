S = input()
T = list(input())

while T:
    if "".join(T) == S:
        print(1)
        exit()
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T = T[::-1]
print(0)