def solution(s):
    total = 0
    c = len(s)
    for i in range(c):
        total += func(s)
        s += s[0]
        s = s[1:]
        
    return total

def func(s):
    l = [""]
    for i in s:
        if i == ")":
            if l[-1] == "(":
                l.pop()
            else:
                l.append(i)
        elif i == "}":
            if l[-1] == "{":
                l.pop()
            else:
                l.append(i)
        elif i == "]":
            if l[-1] == "[":
                l.pop()
            else:
                l.append(i)
        else:
             l.append(i)   
    if len(l) == 1:
        return 1
    else:
        return 0
                
            
    