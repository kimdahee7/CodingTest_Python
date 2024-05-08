name = input()
l = len(name)
result = ["0"] * l
name = sorted(name)
i = 0
while name:
    if len(name) == 1:
        result[l//2] = name[0]
        name.pop(0)
    elif name[0] == name[1]:
        result[i] = name[0]
        result[l-i-1] = name[1]
        name.pop(0)
        name.pop(0)
        i +=1
    else:
        result[l//2] = name[0]
        name.pop(0)

if "0" in result:
    print("I'm Sorry Hansoo")
else:
    print("".join(result))