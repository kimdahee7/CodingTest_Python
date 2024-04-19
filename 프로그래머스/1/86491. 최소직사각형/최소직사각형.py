def solution(sizes):
    answer = 0
    l1 = []
    l2 = []
    for i in sizes:
        l1.append(max(i))
        l2.append(min(i))
    answer = max(l1) * max(l2)
    return answer