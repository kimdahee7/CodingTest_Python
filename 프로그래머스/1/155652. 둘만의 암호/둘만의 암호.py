def solution(s, skip, index):
    answer = ''
    l = []
    for i in range(ord('a'),ord('z')+1):
        if chr(i) not in skip:
            l.append(chr(i))
    for i in s:
        ind = l.index(i)
        answer += l[(ind+index)%len(l)]
    return answer