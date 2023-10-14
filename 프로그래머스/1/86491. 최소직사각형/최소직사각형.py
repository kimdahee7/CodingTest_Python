def solution(sizes):
    answer = 0
    b = set()
    s = set()
    for i in sizes:
        if i[0] >= i[1]:
            b.add(i[0])
            s.add(i[1])
        else:
            b.add(i[1])
            s.add(i[0])
    answer = max(b)*max(s) 
    return answer