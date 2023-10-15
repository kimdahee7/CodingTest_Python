def solution(answers):
    answer = []
    l = []
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    l.append(func(n1,answers))
    l.append(func(n2,answers))
    l.append(func(n3,answers))
    max_data = max(l)
    for i in range(len(l)):
        if l[i] == max_data:
            answer.append(i+1)
    return answer

def func(n,answers):
    total = 0
    if len(n) > len(answers):
        for i in range(len(answers)):
            if answers[i] == n[i]:
                total +=1
        return total
    else: 
        m = len(answers)//len(n)
        n = n*(m+1)
        for k in range(len(answers)):
            if answers[k] == n[k]:
                total +=1
        return total
            