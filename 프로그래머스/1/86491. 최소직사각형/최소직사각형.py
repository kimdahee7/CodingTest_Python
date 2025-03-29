def solution(sizes):
    answer = 0
    w = []
    h = []
    for s in sizes:
        s.sort()
        w.append(s[1])
        h.append(s[0])
    answer = max(w) * max(h)
    return answer